*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#mdn-search)
    

Import attributes
=================

Baseline 2025

Newly available

\*

Since April 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** A previous version of this proposal used the `assert` keyword instead of `with`. The assertion feature is now non-standard. Check the [browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#browser_compatibility)
 for details.

The **import attributes** feature instructs the runtime about how a module should be [loaded](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
, including the behavior of module resolution, [fetching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
, parsing, and [evaluation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#evaluating_modules)
. It's supported in [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declarations, [`export...from`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#re-exporting_aggregating)
 declarations, and dynamic [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
.

Attributes can be attached to any kind of `import`/`export from` statement, including default import, namespace import, etc. They follow the module specifier string and start with the `with` keyword. When used with `import()`, the attributes are specified in the `options` parameter as the `with` property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#syntax)

----------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#parameters)

[`keyN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#keyn)

An attribute key. Can be an identifier or a string literal. All keys must be unique and must be known to the runtime.

[`"dataN"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#datan)

An attribute value. Must be a string literal.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

An unsupported `key` was specified in a _static import_.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

An unsupported `key` was specified in a _dynamic import_.

Note that specifying an unsupported value for a supported key may also result in an exception in some cases, depending on the key.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#description)

--------------------------------------------------------------------------------------------------------------------

Import attributes tell the runtime how a particular module should be loaded.

The primary use case is to load non-JS modules, such as JSON modules and CSS modules. Consider the following statement:

On the web, loading an uncached module from an HTTP URL involves an HTTP request. The response is then prepared into a JavaScript value and made available to the program by the runtime. For example, the response may look like this:

Modules are identified and parsed only according to their served [media type (MIME type)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)
 — the file extension in the URL cannot be used to identify a file's type. In this case, the MIME type is `application/json`, which tells the browser that the file is JSON and must be parsed as JSON. If, for some reason (e.g., the server is hijacked or bogus), the media type in the server response is set to `text/javascript` (for JavaScript source), then the file would be parsed and executed as code. If the "JSON" file actually contains malicious code, the `import` declaration would unintentionally execute external code, posing a serious security threat.

Import attributes fix this problem by allowing the author to explicitly specify how a module should be validated. In particular, the `type` attribute allows you to validate that the file is served with a particular media type, and fails the import if a different media type is used.

For example, the code above can be written to specify that the expected type is `"json"` and the import would fail if it was served with `text/javascript` (or any media type other than a JSON MIME type like `application/json`):

The `type` attribute allows you to specify that modules are served as JSON, CSS, or plain text (and implicitly as JavaScript).

Other attributes may also be supported, and [can affect the behavior of different parts of the loading process](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#intended_semantics_for_import_attributes)
. A syntax error is thrown if an unknown attribute is used in a static import; a dynamic import rejects with a type error.

### [Standard attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#standard_attributes)

The available attributes depend on the language and runtime environment. The ECMAScript standard [defines the `type` attribute with the values `"json"` and `"text"`](https://tc39.es/ecma262/multipage/ecmascript-language-scripts-and-modules.html#sec-HostLoadImportedModule "External link (opens in new tab)")
.

The HTML specification also [defines the `type` attribute with values `"json"`, `"text"` and `"css"`](https://html.spec.whatwg.org/multipage/webappapis.html#module-type-allowed "External link (opens in new tab)")
 — these are the attributes that are supported in browser environments.

#### JSON Modules (`{ type: "json" }`)

The `json` type indicates that the imported file must contain JSON. You can load JSON from a file into the `data` object using the following code:

If the file is served with any other media type than a JSON MIME type, the import will fail.

The `type` attribute changes how the module is fetched (the browser sends the request with ``[`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept) : application/json`` header), but does _not_ change how the module is parsed or evaluated. The runtime already knows to parse the module as JSON given the response MIME type. It only uses the attribute to do _after-the-fact_ checking that the `data.json` module is, in fact, a JSON module. For example, if the response header changes to `Content-Type: text/javascript` instead, the program will fail with a similar error as above.

The specification explicitly calls out `type: "json"` to be supported — if a module is asserted to be `type: "json"` and the runtime does not fail this import, then it must be parsed as JSON.

However, there's no behavior requirement otherwise: for imports without a `type: "json"` attribute, the runtime may still parse it as JSON if security is not an issue in this environment.

Browsers, on the other hand, implicitly assume that the module is JavaScript if the `type` is not specified, and fail if the module is not JavaScript (for example, JSON). This ensures that module types are always strictly validated and prevents any security risks. Non-browser runtimes such as Node and Deno align with browser semantics and enforce `type` for JSON modules.

In other words, if you omit the `type` and attempt to import a file as `"application/json"` you will usually get an error like the following:

Failed to load module script: Expected a JavaScript module script but the server responded with a MIME type of "application/json". Strict MIME type checking is enforced for module scripts per HTML spec.

#### CSS Modules (`{ type: "css" }`)

The HTML spec defines the `css` type, which imports a stylesheet into a script as a [`CSSStyleSheet`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet)
 object.

The code below shows how you might import a style and add it to your document. The import will throw an exception if `example_styles.css` is served with any media type other than `"text/css"`.

Note that importing CSS modules into workers is usually not supported, because the CSSOM specification only exposes `CSSStyleSheet` in the window context.

#### Text Modules (`{ type: "text" }`)

The `text` type allows importing a module's source as a string value. You can load text from a file into the `text` string using the following code:

The file will be requested with an ``[`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept) : text/plain`` header, but the value of the response's ``[`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) `` header is ignored, and all files are parsed as UTF-8. It can contain any textual data, even JavaScript code (which is treated as plain text).

If possible, prefer [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
 to obtain a compiled module for later instantiation, or [`import defer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)
 to defer the synchronous evaluation of a module. Using `with { type: "text" }` means the module cannot reuse the cache if it was imported somewhere else, and userland evaluation of string sources may be incompatible with strict [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 settings.

### [Intended semantics for import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#intended_semantics_for_import_attributes)

An attribute can change the runtime's behavior at every stage of the module loading process:

*   Resolution: the attributes are part of the module request, alongside the module specifier (the string in the `from` clause). Therefore, given the same string path, different attributes may lead to entirely different modules being loaded. For example, [TypeScript supports the `resolution-mode` attribute](https://devblogs.microsoft.com/typescript/announcing-typescript-5-3/#stable-support-resolution-mode-in-import-types "External link (opens in new tab)")
    .
    
*   Fetching: for example, CSS modules are fetched with the [`destination`](https://developer.mozilla.org/en-US/docs/Web/API/Request/destination)
     set to `"style"`, JSON modules are fetched with `destination: "json"`, and text modules are fetched with `destination: "text"`. This means given the same destination URL, the server may still return different content.
    
*   Parsing and evaluation: the runtime may use the attribute to determine how to parse and evaluate the module.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#examples)

--------------------------------------------------------------------------------------------------------------

### [Importing JSON modules with the type attribute](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#importing_json_modules_with_the_type_attribute)

In `data.json`:

In `index.html`:

Start a local HTTP server (see [using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web)
) and go to the `index.html` page. You should see `Shilpa` on the page.

**Note:** JSON modules only have one default export. You cannot do named imports from them (like `import { name } from "data.json"`).

### [Using import attributes with dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#using_import_attributes_with_dynamic_import)

Import attributes are also accepted as the second parameter of the `import()` syntax.

Note that, like static imports, dynamic imports are cached for the lifetime of the environment (e.g., a page or worker). If you expect this data to change (such as the latest news or a user's credits), use the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
 instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-WithClause](https://tc39.es/ecma262/multipage/ecmascript-language-scripts-and-modules.html#prod-WithClause) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
    
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    
*   [Import attributes proposal](https://github.com/tc39/proposal-import-attributes "External link (opens in new tab)")
    
*   [JSON modules proposal](https://github.com/tc39/proposal-json-modules "External link (opens in new tab)")
    
*   [Import Text proposal](https://github.com/tc39/proposal-import-text "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/import/with/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/import/with (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport%2Fwith&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fimport%2Fwith%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport%2Fwith%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fimport%2Fwith%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")