*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#mdn-search)
    

await using
===========

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/366)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`await using`** declaration declares block-scoped local variables that are _asynchronously disposed_. Like [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, variables declared with `await using` must be initialized and cannot be reassigned. The variable's value must be either `null`, `undefined`, or an object with a [`[Symbol.asyncDispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
 or [`[Symbol.dispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
 method. When the variable goes out of scope, the `[Symbol.asyncDispose]()` or `[Symbol.dispose]()` method of the object is called and awaited, to ensure that resources are freed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#syntax)

----------------------------------------------------------------------------------------------------------

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#namen)

The name of the variable to declare. Each must be a legal JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 and _not_ a [destructuring binding pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`valueN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#valuen)

Initial value of the variable. It can be any legal expression but its value must be either `null`, `undefined`, or an object with a [`[Symbol.asyncDispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
 or [`[Symbol.dispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
 method.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#description)

--------------------------------------------------------------------------------------------------------------------

This declaration can only be used in places where both [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 and [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 can be used, which include:

*   Inside a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
     (if the block is also in an async context)
*   Inside an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
     or async generator function body
*   At the top level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    
*   In the initializer of a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    , [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
     (if the `for` loop is also in an async context), or [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
     loop

An `await using` declares an async disposable resource that's tied to the lifetime of the variable's scope (block, function, module, etc.). When the scope exits, the resource is disposed of asynchronously. Its syntax may be somewhat confusing, because the `await` does not have an awaiting effect when the variable is first declared, but only when the variable goes out of scope.

When a variable is first declared and its value is non-nullish, a _disposer_ is retrieved from the object. The `[Symbol.asyncDispose]` property is tried first, and falls back to `[Symbol.dispose]` if `[Symbol.asyncDispose]` is `undefined`. If neither property contains a function, a `TypeError` is thrown. Notably, the `[Symbol.dispose]()` method is wrapped into a function that looks like `async () => { object[Symbol.dispose](); }`, which means if it returns a promise, that promise is _not_ awaited. This disposer is saved to the scope.

When the variable goes out of scope, the disposer is called and awaited. If the scope contains multiple [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 or `await using` declarations, all disposers are run in sequence in the reverse order of declaration, regardless of the type of declaration. All disposers are guaranteed to run (much like the `finally` block in [`try...catch...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
). All errors thrown during disposal, including the initial error that caused the scope exit (if applicable), are all aggregated inside one [`SuppressedError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError)
, with each earlier exception as the `suppressed` property and the later exception as the `error` property. This `SuppressedError` is thrown after disposal is complete.

The variable is allowed to have value `null` or `undefined`, so the resource can be optionally present. As long as one `await using` variable is declared in this scope, at least one `await` is guaranteed to happen on scope exit, even if the variable actually has value `null` or `undefined`. This prevents the disposal from happening synchronously, causing timing issues (see [control flow effects of `await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#control_flow_effects_of_await)
).

`await using` ties resource management to lexical scopes, which is both convenient and sometimes confusing. See below for some examples where it may not behave how you expect. If you want to hand-manage resource disposal, while maintaining the same error handling guarantees, you can use [`AsyncDisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack)
 instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#examples)

--------------------------------------------------------------------------------------------------------------

You should also check [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 for more examples, especially some general caveats with respect to scope-based resource management.

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#basic_usage)

Usually, you use `await using` on some library-provided resource that already implements the async disposable protocol. For example, the Node.js [`FileHandle`](https://nodejs.org/api/fs.html#filehandlesymbolasyncdispose "External link (opens in new tab)")
 is async disposable:

Note that there are two `await` operations in the declaration for `file`, which do different things and are both necessary. `await fs.open()` causes an await during _acquisition_: it waits for the file to be opened and unwraps the returned promise into a `FileHandle` object. `await using file` causes an await during _disposal_: it makes `file` disposed asynchronously when the variable goes out of scope.

### [`await using` with `for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#await_using_with_for_await...of)

It's very easy to confuse the following three syntaxes:

*   `for await (using x of y) { ... }`
*   `for (await using x of y) { ... }`
*   `for (using x of await y) { ... }`

It may be even more confusing to know that they can be used together.

First, `await y` does what you expect: we [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 the promise `y`, which is expected to resolve to an object we iterate over. Let us set this variant aside.

The [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
 loop requires the `y` object to be an _async iterable_. This means that the object must have a `[Symbol.asyncIterator]` method that returns an _async iterator_, whose `next()` method returns a promise representing the result. This is for when the iterable doesn't know what the next value is, or even if it's done yet, until some async operation is complete.

On the other hand, the `await using x` syntax requires the `x` object, as yielded from the iterable, to be an _async disposable_. This means that the object must have a `[Symbol.asyncDispose]` method that returns a promise representing the disposal operation. This is a separate concern from the iteration itself, and is only called when the variable `x` goes out of scope.

In other words, all of the following four combinations are valid and do different things:

*   `for (using x of y)`: `y` is synchronously iterated, yielding one result at a time, which can be disposed synchronously.
*   `for await (using x of y)`: `y` is asynchronously iterated, yielding one result at a time after awaiting, but the result value can be disposed synchronously.
*   `for (await using x of y)`: `y` is synchronously iterated, yielding one result at a time, but the result value can only be disposed asynchronously.
*   `for await (await using x of y)`: `y` is asynchronously iterated, yielding one result at a time after awaiting, and the result value can only be disposed asynchronously.

Below, we create some fictitious values of `y` to demonstrate their use cases. For asynchronous APIs, we base our code on the Node.js [`fs/promises`](https://nodejs.org/api/fs.html#promises-api "External link (opens in new tab)")
 module.

### [Implicit await on scope exit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#implicit_await_on_scope_exit)

As soon as one `await using` is declared in a scope, the scope will always have an `await` on exit, even if the variable is `null` or `undefined`. This ensures stable execution order and error handling. The [Control flow effects of await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#control_flow_effects_of_await)
 examples have more details on this.

In the example below, the `example()` call below doesn't resolve until one tick after, because of an implicit `await` when the function returns.

Consider the same code but with a synchronous [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 instead. This time, the `example()` call immediately resolves, so the two `then()` handlers are called in the same tick.

For a more realistic example, consider two concurrent calls to a function:

As you can see, the `required 2` resource is disposed in the same tick as `required 1`. If the `optional` resource did not cause a redundant `await`, then `required 2` would have been disposed earlier, which would be simultaneous with `optional`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript Async Explicit Resource Management  <br>\# sec-let-and-const-declarations](https://tc39.es/proposal-async-explicit-resource-management/#sec-let-and-const-declarations) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using#see_also)

--------------------------------------------------------------------------------------------------------------

*   [JavaScript resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
    
*   [`Symbol.asyncDispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
    
*   [`AsyncDisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 26, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/await_using/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/await_using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fawait_using&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fawait_using%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fawait_using%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fawait_using%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F419694495e070daaf466c923b413b3f476740fd6%0A*+Document+last+modified%3A+2025-11-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")