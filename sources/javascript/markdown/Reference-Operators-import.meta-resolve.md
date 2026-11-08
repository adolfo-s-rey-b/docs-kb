*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#mdn-search)
    

import.meta.resolve()
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`import.meta.resolve()`** is a built-in function defined on the [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
 object of a JavaScript module that resolves a module specifier to a URL using the current module's URL as base.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#syntax)

-----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#parameters)

[`moduleName`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#modulename)

A string that specifies a potentially importable module. This may be a relative path (such as `"./lib/helper.js"`), a bare name (such as `"my-module"`), or an absolute URL (such as `"https://example.com/lib/helper.js"`).

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#return_value)

Returns a string corresponding to the path that would be imported if the argument were passed to [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#description)

---------------------------------------------------------------------------------------------------------------------------

`import.meta.resolve()` allows a script to access the _module specifier resolution_ algorithm for a name, like this:

Note that `import.meta.resolve()` only performs resolution and does not attempt to [load](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 or import the resulting module. In browsers, its return value is the same _regardless of whether the returned URL corresponds to a file that exists, and regardless of whether that file contains valid code for a module_. The operation is _synchronous_. Non-browser hosts may inspect the file system during resolution; for example, Node.js can read package metadata and check paths.

It is different from [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
, because although both accept a module specifier as the first argument, `import.meta.resolve()` returns the path that _would be imported_ without making any attempt to access that path. Therefore, the following two are effectively the same code:

However, even if `"./lib/helper.js"` cannot be successfully imported, the second snippet will not encounter an error until it attempts to perform the import on line 2.

### [Bare module names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#bare_module_names)

You can pass a bare module name (also known as a bare module specifier) to `import.meta.resolve()`, as long as module resolution is defined for the name. For example, you can define this using an [import map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)
 inside a browser:

Again, since this snippet does not try to import `moduleEntryPath` — neither does the import map — it prints the resolved URL regardless of whether `./modules/my-module/index.js` actually exists.

### [Comparison with new URL()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#comparison_with_new_url)

The [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL)
 constructor accepts a second _base URL_ argument. When the first argument is a relative path and the base URL is [`import.meta.url`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#value)
, the effect is similar to `import.meta.resolve()`.

This is also a useful replacement syntax when targeting older browsers. However, there are some differences:

*   `import.meta.resolve()` returns a string, while `new URL()` returns a `URL` object. It is possible to use [`href`](https://developer.mozilla.org/en-US/docs/Web/API/URL/href)
     or [`toString()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/toString)
     on the constructed `URL`, but this may still not produce the exact same result in some JavaScript environments or when using tools like bundlers to statically analyze the code.
*   `import.meta.resolve()` is aware of additional resolution configurations, such as resolving bare module names using import maps, as described above. `new URL()` is not aware of import maps and treats bare module names as relative paths (i.e., `new URL("my-module", import.meta.url)` means `new URL("./my-module", import.meta.url)`).

Some tools recognize `new URL("./lib/helper.js", import.meta.url).href` as a dependency on `"./lib/helper.js"` (similar to an import), and take this into account for features like bundling, rewriting imports for moved files, "go to source" functionality, etc. However, since `import.meta.resolve()` is less ambiguous and specifically designed to indicate a module path resolution dependency, you should use `import.meta.resolve(moduleName)` instead of `new URL(moduleName, import.meta.url)` for these use cases wherever possible.

### [Not an ECMAScript feature](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#not_an_ecmascript_feature)

`import.meta.resolve()` is not specified or documented as part of the [ECMAScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#javascript_the_core_language_ecmascript)
 for JavaScript modules. Instead, the specification defines [the `import.meta` object](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ImportMeta "External link (opens in new tab)")
 but [leaves all its properties as "host-defined"](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-hostgetimportmetaproperties "External link (opens in new tab)")
. The WHATWG HTML standard picks up where the ECMAScript standard leaves off, and [defines `import.meta.resolve`](https://html.spec.whatwg.org/multipage/webappapis.html#hostgetimportmetaproperties "External link (opens in new tab)")
 using its [module specifier resolution](https://html.spec.whatwg.org/multipage/webappapis.html#resolve-a-module-specifier "External link (opens in new tab)")
.

This means that `import.meta.resolve()` is not required to be implemented by all conformant JavaScript implementations. However, `import.meta.resolve()` may also be available in non-browser environments:

*   Deno implements [compatibility with browser behavior](https://docs.deno.com/api/node/module/#ImportMeta.methods "External link (opens in new tab)")
    .
*   Node.js also implements [the `import.meta.resolve()` function](https://nodejs.org/docs/latest/api/esm.html#importmetaresolvespecifier "External link (opens in new tab)")
    , but adds an additional `parent` parameter if you use the `--experimental-import-meta-resolve` flag.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#examples)

---------------------------------------------------------------------------------------------------------------------

### [Resolve a path for the Worker() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#resolve_a_path_for_the_worker_constructor)

`import.meta.resolve()` is particularly valuable for APIs that take a path to a script file as an argument, such as the [`Worker()`](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker)
 constructor:

This is also useful to calculate paths for other workers, such as [service workers](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorker)
 and [shared workers](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker)
. However, if you are using a relative path to calculate the URL of a service worker, keep in mind that the directory of the resolved path determines its [registration scope](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/scope)
 by default (although a different scope can be specified [during registration](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register)
).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# import-meta-resolve](https://html.spec.whatwg.org/multipage/webappapis.html#import-meta-resolve) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    
*   [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/import.meta/resolve/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/import.meta/resolve (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport.meta%2Fresolve&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport.meta%2Fresolve%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport.meta%2Fresolve%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport.meta%2Fresolve%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")