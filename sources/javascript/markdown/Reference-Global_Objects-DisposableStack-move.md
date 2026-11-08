*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#mdn-search)
    

DisposableStack.prototype.move()
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/366)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`move()`** method of [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
 instances creates a new `DisposableStack` instance that contains the same disposers as this stack, and then marks this stack as disposed, without calling any disposers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#syntax)

-----------------------------------------------------------------------------------------------------------------------

js

    move()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#return_value)

A new [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
 instance.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#exceptions)

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

Thrown if the stack is already disposed.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#description)

---------------------------------------------------------------------------------------------------------------------------------

The primary purpose of `move()` is to enable transferring responsibility for disposal out of the current scope. For example, your function can claim ownership of some resources and dispose them if an error occurs; if everything completes successfully, then you return these resources and transfer ownership to the caller.

When using `move()` to transfer ownership, calling `move()` should be the very last step in your control flow, because there will be no owner in between your code dropping ownership via `move()` and the caller picking up ownership from the return value.

js

    let resource1;
    
    function init() {
      using disposer = new DisposableStack();
      resource1 = disposer.use(getResource1());
      // ...
      // Drop ownership immediately before returning
      return disposer.move();
    }
    
    // Pick up ownership immediately after returning
    using disposer = init();
    

js

    let resource1;
    
    function init() {
      using disposer = new DisposableStack();
      resource1 = disposer.use(getResource1());
      // ...
      const newDisposer = disposer.move();
      // If someone adds code in between these lines and an error occurs,
      // there would be no owner to free resource1
      return newDisposer;
    }
    
    using disposer = init();
    

Also be cautious with the following pattern, although using the "good" pattern may be very awkward in many cases:

js

    function init() {
      using disposer = new DisposableStack();
      const resource1 = disposer.use(getResource1());
      // ...
      return { disposer: disposer.move(), resource1 };
    }
    
    const { resource1, ...rest } = init();
    // If someone adds code in between these lines and an error occurs,
    // there would be no owner to free resource1
    using disposer = rest.disposer;
    

`move()` can also be used for conditional disposal in cases where you may sometimes not want to dispose the resources at all. For example:

js

    using disposer = new DisposableStack();
    const server = disposer.use(makeServer());
    await server.init();
    if (server.ready) {
      // Successfully initialized server; it now should live through the rest
      // of the program. Drop its disposer and don't pick it up. It will no
      // longer be disposed at all.
      disposer.move();
    }
    // If we reach the end of the scope without running disposer.move(),
    // then server isn't ready for any reason, and we dispose its resources
    // by disposing the disposer.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Claiming ownership of a stack](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#claiming_ownership_of_a_stack)

js

    function consumeStack(stack) {
      using newStack = stack.move(); // newStack now owns the disposers
      console.log(stack.disposed); // true
      console.log(newStack.disposed); // false
      // newStack is disposed here immediately before the function exits
    }
    
    const stack = new DisposableStack();
    console.log(stack.disposed); // false
    consumeStack(stack);
    console.log(stack.disposed); // true
    

### [Allowing resources to be disposed within two code paths](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#allowing_resources_to_be_disposed_within_two_code_paths)

The major use case of `move()` is when you have one or more resources which could either be disposed right here or could be persisted for later use. In this case, you can put the resources in a `DisposableStack` and then call `move()` when you need to persist the resources for later usage.

js

    class PluginHost {
      #disposed = false;
      #disposables;
      #channel;
      #socket;
    
      constructor() {
        // Create a DisposableStack that is disposed when the constructor exits.
        // If construction succeeds, we move everything out of `disposer` and into
        // `#disposables` to be disposed later.
        using disposer = new DisposableStack();
    
        // Create an IPC adapter around process.send/process.on("message").
        // When disposed, it unsubscribes from process.on("message").
        this.#channel = disposer.use(new NodeProcessIpcChannelAdapter(process));
    
        // Create a pseudo-websocket that sends and receives messages over
        // a NodeJS IPC channel.
        this.#socket = disposer.use(new NodePluginHostIpcSocket(this.#channel));
    
        // If we made it here, then there were no errors during construction and
        // we can safely move the disposables out of `disposer` and into `#disposables`.
        this.#disposables = disposer.move();
    
        // If construction failed, then `disposer` would be disposed before reaching
        // the line above. Event handlers would be removed, allowing `#channel` and
        // `#socket` to be GC'd.
      }
    
      [Symbol.dispose]() {
        if (this.#disposed) {
          return;
        }
        this.#disposed = true;
        // Put `this.#disposables` into a `using` variable, so it is automatically
        // disposed when the function exits.
        using disposables = this.#disposables;
    
        // NOTE: we can free `#socket` and `#channel` here since they will be
        // disposed by the call to `disposables[Symbol.dispose]()`, below.
        // This isn't strictly a requirement for every disposable, but is
        // good housekeeping since these objects will no longer be useable.
        this.#socket = undefined;
        this.#channel = undefined;
        this.#disposables = undefined;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript Async Explicit Resource Management  <br>\# sec-disposablestack.prototype.move](https://tc39.es/proposal-async-explicit-resource-management/#sec-disposablestack.prototype.move) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `DisposableStack.prototype.move` in `core-js`](https://core-js.io/docs/features/ecmascript/explicit-resource-management "External link (opens in new tab)")
    
*   [JavaScript resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    
*   [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
    
*   [`DisposableStack.prototype.dispose()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/dispose)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/disposablestack/move/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/disposablestack/move (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDisposableStack%2Fmove&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdisposablestack%2Fmove%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDisposableStack%2Fmove%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdisposablestack%2Fmove%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")