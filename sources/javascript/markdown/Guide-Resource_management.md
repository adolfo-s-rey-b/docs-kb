*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#mdn-search)
    

JavaScript resource management
==============================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
    

This guide talks about how to do _resource management_ in JavaScript. Resource management is not exactly the same as [memory management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management)
, which is a more advanced topic and usually handled automatically by JavaScript. Resource management is about managing resources that are _not_ automatically cleaned up by JavaScript. Sometimes, it's okay to have some unused objects in memory, because they don't interfere with application logic, but resource leaks often lead to things not working, or a lot of excess memory usage. Therefore, this is not an optional feature about optimization, but a core feature to write correct programs!

**Note:** While memory management and resource management are two separate topics, sometimes you can hook into the memory management system to do resource management, as a last resort. For example, if you have a JavaScript object representing a handle of an external resource, you can create a [`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
 to clean up the resource when the handle is garbage collected, because there is definitely no way to access the resource afterwards. However, there is no guarantee that the finalizer will run, so it's not a good idea to rely on it for critical resources.

[Problem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#problem)

-----------------------------------------------------------------------------------------------------

Let's first look at a few examples of resources that need to be managed:

*   **File handles**: A file handle is used to read and write bytes in a file. When you are done with it, you must call [`fileHandle.close()`](https://nodejs.org/api/fs.html#filehandleclose "External link (opens in new tab)")
    , otherwise the file will remain open, even when the JS object is no longer accessible. As the linked Node.js docs say:
    
    > If a `<FileHandle>` is not closed using the `fileHandle.close()` method, it will try to automatically close the file descriptor and emit a process warning, helping to prevent memory leaks. Please do not rely on this behavior because it can be unreliable and the file may not be closed. Instead, always explicitly close `<FileHandle>`s. Node.js may change this behavior in the future.
    
*   **Network connections**: Some connections, such as [`WebSocket`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
     and [`RTCPeerConnection`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection)
    , need to be closed if no messages are transmitted. Otherwise, the connection remains open, and connection pools are often very limited in size.
    
*   **Stream readers**: If you don't call [`ReadableStreamDefaultReader.releaseLock()`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader/releaseLock)
    , the stream will be locked and does not permit another reader to consume it.
    

Here is one concrete example, using a readable stream:

Here, we have a stream that emits three chunks of data. We read from the stream until we find the letter "b". When `readUntil` returns, the stream is only partially consumed, so we should be able to continue to read from it using another reader. However, we forgot to release the lock, so although `reader` is no longer available, the stream is still locked and we cannot create another reader.

The solution in this case is straightforward: call `reader.releaseLock()` at the end of `readUntil`. But, a few issues still remain:

*   Inconsistency: different resources have different ways to release them. For example, we have `close()`, `releaseLock()`, `disconnect()`, etc. The pattern does not generalize.
    
*   Error handling: what happens if the `reader.read()` call fails? Then `readUntil` would terminate and never get to the `reader.releaseLock()` call. We can fix this using [`try...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    :
    
    But you have to remember to do this every time you have some important resource to release.
    
*   Scoping: in the above example, `reader` is already closed when we exit the `try...finally` statement, but it continues to be available in its scope. This means you may accidentally use it after it's closed.
    
*   Multiple resources: if we have two readers on different streams, we have to remember to release both of them. This is a respectable attempt to do so:
    
    However, this introduces more error handling troubles. If `stream2.getReader()` throws, then `reader1` does not get released; if `reader1.releaseLock()` throws an error, then `reader2` does not get released. This means we actually have to wrap each resource acquisition-release pair in its own `try...finally`:
    

You see how a seemingly benign task of calling `releaseLock` can quickly lead to nested boilerplate code. This is why JavaScript provides integrated language support for resource management.

[The `using` and `await using` declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#the_using_and_await_using_declarations)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The solution we have is two special kinds of variable declaration: [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 and [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
. They are similar to `const`, but they automatically release the resource when the variable goes out of scope as long as the resource is _disposable_. Using the same example as above, we can rewrite it as:

**Note:** At the time of writing, [`ReadableStreamDefaultReader`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader)
 does not implement the disposable protocol. This is a hypothetical example.

First, notice the extra braces around the code. This creates a new [block scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 for the `using` declarations. Resources declared with `using` are automatically freed when they go out of the scope of `using`, which, in this case, is whenever we are exiting the block, either because all statements have executed, or because an error or `return`/`break`/`continue` was encountered somewhere.

This means `using` can only be used in a scope that has a clear lifetime—namely, it cannot be used at the top level of a script, because variables at the top level of a script are in scope for all future scripts on the page, which practically means the resource can never be freed if the page never unloads. However, you can use it at the top level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
, because the module scope ends when the module finishes executing.

Now we know _when_ `using` does cleanup. But _how_ is it done? `using` requires the resource to implement the _disposable_ protocol. An object is disposable if it has the [`[Symbol.dispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
 method. This method is called with no arguments to perform cleanup. For example, in the reader case, the `[Symbol.dispose]` property can be a simple alias or wrapper of `releaseLock`:

Through the disposable protocol, `using` can dispose all resources in a consistent fashion without understanding what type of resource it is.

Every scope has a list of resources associated with it, in the order they were declared. When the scope exits, the resources are disposed in reverse order, by calling their `[Symbol.dispose]()` method. For example, in the example above, `reader1` is declared before `reader2`, so `reader2` is disposed first, then `reader1`. Errors thrown when attempting to dispose one resource will not prevent disposal of other resources. This is consistent with the `try...finally` pattern, and respects possible dependencies between resources.

`await using` is very similar to `using`. The syntax tells you that an `await` happens somewhere—not when the resource is declared, but actually when it's disposed. `await using` requires the resource to be _async disposable_, which means it has a [`[Symbol.asyncDispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
 method. This method is called with no arguments and returns a promise that resolves when the cleanup is done. This is useful when the cleanup is asynchronous, such as `fileHandle.close()`, in which case the result of the disposal can only be known asynchronously.

Because `await using` requires doing an `await`, it is only permitted in contexts where `await` is, which includes inside `async` functions and top-level `await` in modules.

Resources are cleaned up sequentially, not concurrently: the return value of one resource's `[Symbol.asyncDispose]()` method will be `await`ed before the next resource's `[Symbol.asyncDispose]()` method is called.

Some things to note:

*   `using` and `await using` are _opt in_. If you declare your resource using `let`, `const`, or `var`, no automatic disposal happens, just like any other non-disposable values.
*   `using` and `await using` require the resource to be disposable (or async disposable). If the resource does not have the `[Symbol.dispose]()` or `[Symbol.asyncDispose]()` method respectively, you will get a `TypeError` at the line of declaration. The resource can be `null` or `undefined`, however, allowing you to conditionally acquire resources.
*   Like `const`, `using` and `await using` variables cannot be re-assigned, although the properties of the objects they hold can be changed. However, the `[Symbol.dispose]()`/`[Symbol.asyncDispose]()` method is already saved at the time of declaration, so changing the method after the declaration does not affect the cleanup.
*   There are some gotchas when conflating scopes with resource lifetime. See [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#examples)
     for a few examples.

[The `DisposableStack` and `AsyncDisposableStack` objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#the_disposablestack_and_asyncdisposablestack_objects)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`using` and `await using` are special syntaxes. Syntaxes are convenient and hide a lot of the complexity, but sometimes you need to do things manually.

For one common example: what if you don't want to dispose the resource at the end of _this_ scope, but at some _later_ scope? Consider this:

As we said, `using` is like `const`: it must be initialized and can't be reassigned, so you may attempt this:

However, this means all logic has to be written inside the `if` or `else`, causing a lot of duplication. What we want to do is to acquire and register the resource in one scope but dispose it in another. We can use a [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
 for this purpose, which is an object which holds a collection of disposable resources and which itself is disposable:

You may have a resource that does not yet implement the disposable protocol, so it will be rejected by `using`. In this case, you can use [`adopt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/adopt)
.

You may have a disposal action to perform but it's not "tethered" to any resource in particular. Maybe you just want to log a message saying "All database connections closed" when there are multiple connections open simultaneously. In this case, you can use [`defer()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/defer)
.

You may want to do _conditional_ disposal—for example, only dispose claimed resources when an error occurred. In this case, you can use [`move()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move)
 to preserve the resources which would otherwise be disposed.

`AsyncDisposableStack` is like `DisposableStack`, but for use with async disposable resources. Its `use()` method expects an async disposable, its `adopt()` method expects an async cleanup function, and its `dispose()` method expects an async callback. It provides a `[Symbol.asyncDispose]()` method. You can still pass it sync resources if you have a mix of both sync and async.

The reference for [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
 contains more examples and details.

[Error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#error_handling)

-------------------------------------------------------------------------------------------------------------------

A major use case of the resource management feature is to ensure that resources are always disposed, even when an error occurs. Let us investigate some complex error handling scenarios.

We start with the following code, which, by using `using`, is robust against errors:

Suppose that `chunk` turns out to be `null`. Then `!chunk.done` will throw a `TypeError`, causing the function to terminate. Before the function exits, `stream[Symbol.dispose]()` is called, which releases the lock on the stream.

So, `using` does not swallow any errors: all errors that occur are still thrown, but the resources get closed right before that. Now, what happens if the resource cleanup itself also throws an error? Let's use a more contrived example:

There are two errors generated in the `doSomething()` call: an error thrown during `doSomething`, and an error thrown during disposal of `reader` because of the first error. Both errors are thrown together, so what you caught is a [`SuppressedError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError)
. This is a special error that wraps two errors: the [`error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError/error)
 property contains the later error, and the [`suppressed`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError/suppressed)
 property contains the earlier error, which gets "suppressed" by the later error.

If we have more than one resource, and _both_ of them throw an error during disposal (this should be exceedingly rare–it's already rare for disposal to fail!), then each earlier error is suppressed by the later error, forming a chain of suppressed errors.

*   The `reader` is released last, so its error is the latest and therefore suppresses everything else: it shows up as `e.error`.
*   The `writer` is released first, so its error is later than the original exiting error, but earlier than the `reader` error: it shows up as `e.suppressed.error`.
*   The original error about "Failed to read" is the earliest error, so it shows up as `e.suppressed.suppressed`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#examples)

-------------------------------------------------------------------------------------------------------

### [Automatically releasing object URLs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#automatically_releasing_object_urls)

In the following example, we create an [object URL](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/blob)
 to a blob (in a real application, this blob would be fetched from somewhere, such as a file or a fetch response) so we can download the blob as a file. In order to prevent a resource leak, we must free the object URL with [`URL.revokeObjectURL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL_static "URL.revokeObjectURL()")
 when it is no longer needed (that is, when the download has successfully started). Because the URL itself is just a string and therefore doesn't implement the disposable protocol, we cannot directly declare `url` with `using`; therefore, we create a `DisposableStack` to serve as the disposer for `url`. The object URL is revoked as soon as `disposer` goes out of scope, which is when either `link.click()` finishes or an error occurs somewhere.

### [Automatically canceling in-progress requests](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#automatically_canceling_in-progress_requests)

In the following example, we [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)
 a list of resources concurrently using [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
. `Promise.all()` fails and rejects the resulting promise as soon as one request failed; however, the other pending requests continue to run, despite their results being inaccessible to the program. To avoid these remaining requests needlessly consuming resources, we need to automatically cancel in-progress requests whenever `Promise.all()` settles. We implement cancellation with an [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
, and pass its [`signal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal "signal")
 to every `fetch()` call. If `Promise.all()` fulfills, then the function returns normally and the controller aborts, which is harmless because there's no pending request to cancel; if `Promise.all()` rejects and the function throws, then the controller aborts and cancels all pending requests.

[Pitfalls](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#pitfalls)

-------------------------------------------------------------------------------------------------------

The resource disposal syntax offers a lot of strong error handling guarantees that ensure the resources are always cleaned up no matter what happens, but there are some pitfalls you may still encounter:

*   Forgetting to use `using` or `await using`. The resource management syntax is only there to help you when you know you need it, but there's nothing to yell at you if you forget to use it! Unfortunately, there's no good way to prevent this before-the-fact, because there are no syntactic clues that something is a disposable resource, and even for disposable resources, you may want to declare them without automatic disposal. You probably need a type checker combined with a linter to catch these issues, such as [typescript-eslint](https://typescript-eslint.io/ "External link (opens in new tab)")
     ([which is still planning to work on this feature](https://github.com/typescript-eslint/typescript-eslint/issues/8255 "External link (opens in new tab)")
    ).
*   Use-after-free. Generally, the `using` syntax ensures that a resource is freed when it goes out of scope, but there are many ways to persist a value beyond its binding variable. JavaScript does not have an ownership mechanism like Rust, so you can declare an alias that doesn't use `using`, or preserve the resource in a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
    , etc. The [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
     reference contains many examples of such pitfalls. Again, there's no good way to properly detect this in a complicated control flow, so you need to be careful.

The resource management feature is not a silver bullet. It is definitely an improvement over manually invoking the disposal methods, but it is not smart enough to prevent all resource management bugs. You still need to be careful and understand the semantics of the resources you are using.

[Conclusion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management#conclusion)

-----------------------------------------------------------------------------------------------------------

Here are the key components of the resource management system:

*   [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
     and [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
     declarations for automatic resource disposal.
*   The _disposable_ and _async disposable_ protocols, using the [`Symbol.dispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
     and [`Symbol.asyncDispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
     respectively, for resources to implement.
*   The [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
     and [`AsyncDisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack)
     objects for cases where `using` and `await using` are not suitable.

With proper usage of these APIs, you can create systems interacting with external resources that remain strong and robust against all error conditions without lots of boilerplate code.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/resource_management/index.md?plain=1 "Folder: en-us/web/javascript/guide/resource_management (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FResource_management&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fresource_management%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FResource_management%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fresource_management%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4b111fc009d4844d407dd1b5c791c07b0fb326fc%0A*+Document+last+modified%3A+2026-09-11T00%3A24%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")