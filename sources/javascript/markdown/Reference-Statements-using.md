*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#mdn-search)
    

using
=====

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/366)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`using`** declaration declares block-scoped local variables that are _synchronously disposed_. Like [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, variables declared with `using` must be initialized and cannot be reassigned. The variable's value must be either `null`, `undefined`, or an object with a [`[Symbol.dispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
 method. When the variable goes out of scope, the `[Symbol.dispose]()` method of the object is called, to ensure that resources are freed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#syntax)

----------------------------------------------------------------------------------------------------

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#namen)

The name of the variable to declare. Each must be a legal JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 and _not_ a [destructuring binding pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`valueN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#valuen)

Initial value of the variable. It can be any legal expression but its value must be either `null`, `undefined`, or an object with a `[Symbol.dispose]()` method.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#description)

--------------------------------------------------------------------------------------------------------------

This declaration can be used:

*   Inside a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
    
*   Inside any [function body](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
     or [class static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    
*   At the top level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    
*   In the initializer of a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    , [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    , or [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
     loop

Most notably, it cannot be used:

*   At the top level of a script, because script scopes are persistent.
*   At the top level of a [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
     statement.
*   In the initializer of a [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
     loop. Because the loop variable can only be a string or symbol, this doesn't make sense.

A `using` declares a disposable resource that's tied to the lifetime of the variable's scope (block, function, module, etc.). When the scope exits, the resource is disposed of synchronously. The variable is allowed to have value `null` or `undefined`, so the resource can be optionally present.

When the variable is first declared and its value is non-nullish, a _disposer_ is retrieved from the object. If the `[Symbol.dispose]` property doesn't contain a function, a `TypeError` is thrown. This disposer is saved to the scope.

When the variable goes out of scope, the disposer is called. If the scope contains multiple `using` or [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
 declarations, all disposers are run in the reverse order of declaration, regardless of the type of declaration. All disposers are guaranteed to run (much like the `finally` block in [`try...catch...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
). All errors thrown during disposal, including the initial error that caused the scope exit (if applicable), are all aggregated inside one [`SuppressedError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError)
, with each earlier exception as the `suppressed` property and the later exception as the `error` property. This `SuppressedError` is thrown after disposal is complete.

`using` ties resource management to lexical scopes, which is both convenient and sometimes confusing. There are many ways to preserve the variable's value when the variable itself is out of scope, so you may hold a reference to an already-disposed resource. See below for some examples where it may not behave how you expect. If you want to hand-manage resource disposal, while maintaining the same error handling guarantees, you can use [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
 instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#examples)

--------------------------------------------------------------------------------------------------------

In the following examples, we assume a simple `Resource` class that has a `getValue` method and a `[Symbol.dispose]()` method:

### [`using` in a block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#using_in_a_block)

The resource declared with `using` is disposed when exiting the block.

### [`using` in a function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#using_in_a_function)

You can use `using` in a function body. In this case, the resource is disposed when the function finishes executing, immediately before the function returns.

Here, `resource[Symbol.dispose]()` will be called after `getValue()`, before the `return` statement executes.

The resource may outlive the declaration, in case it's captured by a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
:

In this case, if you call `example()()`, you will always execute `getValue` on a resource that's already disposed, because the resource was disposed when `example` returns. In case you want to dispose the resource immediately after the callback has been called once, consider this pattern:

Here, we _alias_ a `const`\-declared resource to a `using`\-declared resource, so that the resource is only disposed after the callback is called; note that if it is never called then the resource will never be cleaned up.

### [`using` in a module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#using_in_a_module)

You can use `using` at the top level of a module. In this case, the resource is disposed when the module finishes executing.

`export using` is invalid syntax, but you can `export` a variable declared elsewhere using `using`:

This is still discouraged, because the importer will always receive a disposed resource. Similar to the closure problem, this causes the value of resource to live longer than the variable.

### [`using` with `for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#using_with_for...of)

You can use `using` in the initializer of a `for...of` loop. In this case, the resource is disposed on every loop iteration.

### [Multiple `using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#multiple_using)

The following are two equivalent ways to declare multiple disposable resources:

In both cases, when the scope exits, `resource2` is disposed before `resource1`. This is because `resource2` may have a dependency on `resource1`, so it's disposed first to ensure that `resource1` is still available when `resource2` is disposed.

### [Optional `using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#optional_using)

`using` allows the variable to have a value of `null` or `undefined`, so the resource can be optionally present. This means that, for example, if you are checking the availability of a resource of some kind:

You don't have to do this:

And can instead do this:

### [`using` declaration without using the variable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#using_declaration_without_using_the_variable)

You can achieve automatic resource disposing using `using`, without even using the variable. This is very useful for setting up a context within a block, such as creating a lock:

Note that `_` is a normal identifier, but it's a convention to use it as a "throwaway" variable. To create multiple unused variables, you need to use distinct names, for example by using a variable name prefixed with `_`.

### [Initialization and temporal dead zones](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#initialization_and_temporal_dead_zones)

`using` variables are subject to the same [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
 restriction as `let` and `const` variables. This means that you can't access the variable before the initialization—the valid lifetime of the resource is strictly from its initialization to the end of its scope. This is enables [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization "External link (opens in new tab)")
\-style resource management.

### [Error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#error_handling)

The `using` declaration is the most useful for managing resource disposal in the presence of errors. If you are not careful, some resources may leak because the error prevents code afterwards from executing.

This will successfully catch the error thrown by `handleResource` and log it, and no matter if `handleResource` throws an error or not, the resource is disposed before exiting the `try` block.

Here, if you don't use `using`, you may do something like:

But, if `handleResource()` throws an error, then control never reaches `resource[Symbol.dispose]()`, and the resource is leaked. Furthermore, if you have two resources, then errors thrown in earlier disposals may prevent later disposals from running, leading to more leaks.

Consider a more complicated case where the disposer itself throws an error:

You can inspect the error thrown in your browser's console. It has the following structure:

SuppressedError: An error was suppressed during disposal
  suppressed: SuppressedError: An error was suppressed during disposal
    suppressed: Error: Can't dispose resource1
    error: Error: Error in main block
  error: Error: Can't dispose resource2

As you can see, `error` contains all the errors that were thrown during disposal, as a [`SuppressedError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError)
. Each additional error is added as the `error` property, and the original error is added as the `suppressed` property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript Async Explicit Resource Management  <br>\# sec-let-and-const-declarations](https://tc39.es/proposal-async-explicit-resource-management/#sec-let-and-const-declarations) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using#see_also)

--------------------------------------------------------------------------------------------------------

*   [JavaScript resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
    
*   [`Symbol.dispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
    
*   [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/using/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fusing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fusing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fusing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fusing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F075e089ec955f14ed65dfaa0bf3311051c58f666%0A*+Document+last+modified%3A+2026-01-28T10%3A43%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")