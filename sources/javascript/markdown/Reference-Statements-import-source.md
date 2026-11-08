*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#mdn-search)
    

import source
=============

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#browser_compatibility)
 carefully before using this in production.

The **`import source`** declaration is similar to the regular [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declaration, except that it results in an object that represents the module's compiled source code. The module is [fetched](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 and compiled, but its dependencies are not [loaded](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 and it is not [linked](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#linking_modules)
 or [evaluated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#evaluating_modules)
. It can be imperatively evaluated later, such as by using [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 or [`WebAssembly.instantiate()`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/instantiate_static)
.

To use `import source`, the target module must be of a kind that supports source phase imports. Currently, only WebAssembly modules support source phase imports, and result in [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module)
 objects. JavaScript module source objects will be added by the [ECMAScript Module Phase Imports](https://github.com/tc39/proposal-esm-phase-imports "External link (opens in new tab)")
 proposal.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#syntax)

------------------------------------------------------------------------------------------------------------

js

    import source x from "module-name";
    

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#x)

Name that will refer to the module source object. Must be a valid JavaScript identifier.

[`module-name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#module-name)

The module to import from. Handled the same way as the [`module-name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#module-name)
 in regular `import` declarations.

[Import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
 are also supported, using a `with` clause after the module specifier.

`source` is not a reserved word. For example, `import source from "./module.js"` is still a regular default import whose local binding is named `source`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the target module does not support source phase imports.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#description)

----------------------------------------------------------------------------------------------------------------------

By default, the `import` declaration performs many tasks at once: resolving the module specifier, fetching the module source code, parsing (potentially discovering transitive dependencies), linking, and evaluating it. This form of eager evaluation is not always desirable, especially when the module source code is intended to be evaluated in some other context, such as a worker thread.

The _import phase modifier_ allows the module import process to stop at a particular phase. By adding `source` after `import`, the source code is parsed and compiled but remains unlinked and unevaluated. The source import does not load the module's transitive dependencies.

Traditionally, the only way to run a part of the pipeline was to manually implement the entirety of it. For example, with WebAssembly, you first use [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
 to retrieve the module's binary bytes, and later compile them using [`WebAssembly.compile()`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/compile_static)
, or compile the response stream using [`WebAssembly.compileStreaming()`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/compileStreaming_static)
, into a `WebAssembly.Module` object.

js

    const myModuleSource = await WebAssembly.compileStreaming(
      fetch("./my-module.wasm"),
    );
    

This kind of manual workflow is problematic for several reasons:

*   It involves too much low-level manipulation, which may be inconsistent with the default module loader's behavior, such as caching, HTTP header settings, and module specifier resolution.
*   It is imperative, making it difficult to reason about the module's dependencies and their evaluation order, especially for bundlers or other analysis tools.
*   Userland evaluation of the raw source code is incompatible with strict [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
     settings.

Using source phase imports avoids these problems.

js

    import source myModuleSource from "./my-module.wasm";
    

The object obtained from this import is an instance of a subclass of [`AbstractModuleSource`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource)
. Each module type that supports source phase imports defines its own subclass. For WebAssembly, the subclass is [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module)
. This object is cached for the specific module so that later source imports resolving to the same module return the exact same object.

Unlike [`import defer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)
, using source import also defers linking. Loading dependencies and linking up front catches missing dependencies or invalid imports before the module is used. Source-phase imports instead leave dependencies unloaded and allow you to control how the module is instantiated. For example, you can instantiate a source-imported WebAssembly module multiple times with different imports, or send it to a worker for instantiation there.

Unlike [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
, the source-imported module is fetched and compiled up front without evaluating it. `import source` also enjoys most benefits of a static declaration, such as better static analysis.

Note that only the "default import" syntax is supported. You cannot use `import source { property } from "./my-module.wasm"`, etc.

### [Importing WebAssembly source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#importing_webassembly_source)

For WebAssembly, you supply the imported values when instantiating the module:

js

    import source myModuleSource from "./my-module.wasm";
    
    const instance = await WebAssembly.instantiate(myModuleSource, {
      env: { log: console.log },
    });
    const { exports } = instance;
    

Unlike an ordinary WebAssembly module import, this creates a new instance with the imports you provide, rather than using the cached instance linked by the module loader. Its `exports` object is not a JavaScript module namespace object. For example, WebAssembly globals are exposed as `WebAssembly.Global` objects through `instance.exports`, whereas the ESM integration exposes their values to JavaScript importers.

**Note:** Support for source phase imports of WebAssembly does not imply support for ordinary WebAssembly module imports. A host may support `import source mod from "./mod.wasm"` while rejecting `import * as ns from "./mod.wasm"`.

Source imports use the host's module loader, including its compilation settings. They are not necessarily equivalent to calling `WebAssembly.compileStreaming()` with default options. For example, [Node.js enables JavaScript string builtins for Wasm imports](https://nodejs.org/api/esm.html#javascript-string-builtins "External link (opens in new tab)")
 and rejects reserved import and export names. Use the direct WebAssembly compilation APIs when you need custom compilation options.

### [Importing JavaScript source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#importing_javascript_source)

For JavaScript (assuming the proposed `import(moduleSource)` support, also in [ECMAScript Module Phase Imports](https://github.com/tc39/proposal-esm-phase-imports "External link (opens in new tab)")
):

js

    import * as namespace from "./my-module.js";
    
    // Is equivalent to:
    
    import source myModuleSource from "./my-module.js";
    
    const namespace = await import(myModuleSource);
    

### [Caching semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#caching_semantics)

The modifier applies to an import, not to the module itself. If another part of the application imports the same module without `source`, the module is evaluated as usual. Both forms share the same module state, and the module's code executes at most once. Changing the import phase does not create a separate module in the cache:

js

    import * as x from "foo";
    import source xSource from "foo";
    
    console.log((await import(xSource)) === x); // true
    

**Note:** This cached instance is reused when you use `import()`, but not when you manually instantiate WebAssembly. Each call to `WebAssembly.instantiate(modSource, imports)` or `new WebAssembly.Instance(modSource, imports)` creates a new instance and runs its initialization, including any start function. In contrast, `WebAssembly.compileStreaming()` only compiles; it does not execute the module or use the ESM module cache.

In contrast, [import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
 can affect module identity. For example, in a host that supports text modules, these two declarations request different module types:

js

    import * as mod from "./module.js";
    import text from "./module.js" with { type: "text" };
    

The two imports are considered to be from different modules that happen to share the same string specifier (on the web, they will be requested with different HTTP headers). The supported attributes and their effects on loading and module identity are defined by the host.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#examples)

----------------------------------------------------------------------------------------------------------------

### [Instantiating a module with different imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#instantiating_a_module_with_different_imports)

Suppose `counter.wasm` imports an immutable `i32` global named `initial` from `env`, initializes an internal counter from it, and exports a function named `increment`. You can reuse its compiled source with different imports and independent internal counters:

js

    import source counterSource from "./counter.wasm";
    
    const first = await WebAssembly.instantiate(counterSource, {
      env: { initial: 0 },
    });
    const second = await WebAssembly.instantiate(counterSource, {
      env: { initial: 100 },
    });
    
    console.log(first.exports.increment()); // 1
    console.log(first.exports.increment()); // 2
    console.log(second.exports.increment()); // 101
    

Each instance has its own internal state, although explicitly imported memories, tables, or other mutable objects can be shared between instances. You can also [send the compiled source to a worker](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module#obtaining_the_module_using_import_source)
 for instantiation there.

### [Exporting a module source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#exporting_a_module_source)

There is no `export source` syntax (see [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#re-exporting_aggregating)
 for more information). You can import a module source and then export its binding without instantiating or evaluating the module:

js

    // -- sources.js --
    import source counterSource from "./counter.wasm";
    
    export { counterSource };
    

js

    // -- main.js --
    import { counterSource } from "./sources.js";
    
    const instance = new WebAssembly.Instance(counterSource, {
      env: { initial: 0 },
    });
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Source Phase Imports  <br>\# sec-imports](https://tc39.es/proposal-source-phase-imports/#sec-imports) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source#see_also)

----------------------------------------------------------------------------------------------------------------

*   [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
     guide
*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`import.source()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source)
    
*   [`AbstractModuleSource`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/import/source/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/import/source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport%2Fsource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fimport%2Fsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport%2Fsource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fimport%2Fsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")