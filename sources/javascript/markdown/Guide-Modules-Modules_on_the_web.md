*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#mdn-search)
    

Using modules on the web
========================

This page discusses how JavaScript modules are integrated with the web platform. Features discussed here are defined in the HTML spec and other web specifications, instead of by the core language, and they are generally only relevant to webpages. If you are writing modules for other environments, you may want to read the [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
 and [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
 guides instead.

[Server configuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#server_configuration)

--------------------------------------------------------------------------------------------------------------------------------------

The first difference you will encounter when migrating web pages to modules is that you can no longer view your HTML using the `file://` protocol. Serve the directory containing your HTML and modules through a [local HTTP server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/set_up_a_local_testing_server)
, then open the page using the server's URL, such as `http://localhost:8000/`.

The reason for this is that module requests use [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
, and `file://` URLs are never same-origin. When importing from another origin, that server must allow your page's origin through its CORS response headers, such as [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin)
. By default, cross-origin module requests are sent without credentials such as cookies. Setting the [`crossorigin="use-credentials"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 attribute on the `<script>` element sends credentials, provided the server's CORS headers allow it (this applies to the whole graph fetched through that script).

The server must send JavaScript modules with a JavaScript [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)
, such as `Content-Type: text/javascript`. Check this for both `.js` and `.mjs` files. If an import fails with a MIME type error, inspect the response in your browser's network tools: a missing file or an HTML fallback page may have been returned instead of the module.

[Applying modules to your HTML](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#applying_modules_to_your_html)

--------------------------------------------------------------------------------------------------------------------------------------------------------

To declare a script is a module in the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element, you need to include `type="module"`. For example, to import the `main.js` script, we use this:

Only the entry point needs a `<script type="module">` element: any modules it imports are loaded as modules automatically, so you don't need to add a `<script>` element just to declare something as a module.

You can also embed the module's script directly into the HTML file by placing the JavaScript code within the body of the `<script>` element:

You should generally define all your modules in separate files. Modules declared inline in HTML can only import other modules, but anything they export will not be accessible by other modules (because they don't have a URL).

You can only use `import` and `export` statements inside modules, not regular scripts. An error will be thrown if your `<script>` element doesn't have the `type="module"` attribute and attempts to import other modules. For example:

[Subresource integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)
 via the [`integrity`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity)
 attribute also works for module scripts, but the attribute only covers the entry module. Integrity metadata for its dependencies can be provided through an import map's `integrity` key.

**Note:** Modules and their dependencies can be preloaded by specifying them in [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements with [`rel="modulepreload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload)
. This can significantly reduce load time when the modules are used.

If you are already familiar with traditional `<script>` elements, here are some more behavior differences to look out for:

*   Within the same environment, a module is only executed once, even if it has been imported multiple times or referenced in multiple `<script>` tags.
*   There is no need to use the `defer` attribute (see [`<script>` attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#attributes)
    ) when loading a module script; module scripts declared in the document without `async` are deferred automatically.
*   Adding the `async` attribute makes the module graph evaluate as soon as it has finished loading, without waiting for HTML parsing to complete and without any ordering guarantee relative to other scripts. Unlike for classic scripts, `async` works on inline module scripts too.

[Modules in workers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#modules_in_workers)

----------------------------------------------------------------------------------------------------------------------------------

Documents aren't the only place where modules run: [workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
 can be modules too. You need to opt into modules by passing `type: "module"` to the [`Worker()`](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker "Worker()")
 or [`SharedWorker()`](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/SharedWorker "SharedWorker()")
 constructor, or to [`navigator.serviceWorker.register()`](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register "navigator.serviceWorker.register()")
:

The worker's file becomes the entry point of its own [module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
.

You can only use `import` declarations or `import()` to import other modules inside a module worker. Calling [`importScripts()`](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/importScripts "importScripts()")
 throws a `TypeError`. Note that dynamic `import()` is not available in service workers, so all of a module service worker's code must be reachable through static imports. [Worklets](https://developer.mozilla.org/en-US/docs/Web/API/Worklet)
 load their code with `addModule()`, which is always a module.

[Module specifiers on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#module_specifiers_on_the_web)

------------------------------------------------------------------------------------------------------------------------------------------------------

Module specifiers are the strings coming after the `from` keyword:

In the [Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#named_imports)
 guide we already said that the module specifier format is runtime-dependent. Let's look at how they work in browsers.

First of all, everything on the web is URL-based. Each module has its URL, so you can import a module by its absolute URL directly:

The browser sends an HTTP request to that given URL, and if the server returns a successful response with `Content-Type: text/javascript`, then the module loading process continues.

**Note:** There's a popular belief that "ESM requires file extensions in module specifiers". This is true and false. The JavaScript runtime does not _add_ an extension for you. If you write `import { name } from "https://example.com/modules/module";`, the browser still sends a request to the URL, without the `.js` extension. If that request succeeds with JavaScript content, the module is still loaded as usual. The only problem is that servers usually interpret extension-less requests to be requests for HTML files, so you almost always need extra configuration to get it serve a JavaScript file for that.

Other URL schemes that you can use as resource locations are supported too, such as [`data:`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
. Read the [`import` reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#module_specifier_resolution)
 for more information.

Always importing from absolute URLs has the same problems as using absolute URLs for link targets: they are long, they don't work if you move your site to another domain, and they don't work if you move your entire JavaScript asset path. The module specifier can also be a relative URL, similar to the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute of [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements. The only difference is that all relative URLs must start with one of `/`, `./`, or `../`—i.e., you cannot use "bare" relative URLs like `modules/module.js`, but must write `./modules/module.js`. This restriction reserves bare specifiers so they can be given special meaning—the ecosystem convention, popularized by Node.js, was that a bare name like `"jquery"` refers to a package. On the web, that special meaning is now assigned by [import maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)
. A bare specifier not remapped by an import map throws a `TypeError`.

The URL in the module specifier is resolved relative to the URL of the current module, not the URL of the HTML document. For example, within a module at `https://example.com/js/main.js`, to import `https://example.com/js/modules/module.js`, write:

[Importing modules using import maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to relative and absolute URLs, [import maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
 allow developers to specify almost any text they want in the module specifier when importing a module; the map provides a corresponding value that will replace the text when the module URL is resolved. The import map is defined using a [JSON object](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#import_map_json_representation)
 inside a `<script>` element with the `type` attribute set to [`importmap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
.

**Note:** An import map only applies to the document — the specification does not define how to apply an import map in a worker or worklet context.

For example, the `imports` key in the import map below defines a "module specifier map" JSON object where the property names can be used as module specifiers, and the corresponding values will be substituted when the browser resolves the module URL.

**Note:** From this point on, we'll omit the wrapping `<script type="importmap">` element and directly present import maps as JSON code. Just keep in mind that the JSON must be inlined in the HTML and cannot be an external file referenced with `src`.

With this map, you can now use bare specifiers like `shapes` and `shapes/square`, which would be rejected by default:

There are many use cases of import maps:

*   They allow modules to be imported using bare module names (as in Node.js), allowing modules that import npm packages to be directly deployed to the web (as long as the packages are also accessible at some URL). See [Literal matching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#literal_matching)
     and [Prefix matching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#prefix_matching)
    .
*   They allow modules imported using full URLs to be swapped out with other URLs as necessary, without changing the source code. See [General URL remapping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#general_url_remapping)
    .
*   They allow particular versions of a library to be imported, based on the path of the script that is importing the module. See [The `scopes` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#the_scopes_object)
    .

This can reduce the effort required to use the same JavaScript libraries in both browser and server.

In addition, the import map also allows module dependencies to have hash integrities (the [`integrity`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity)
 attribute on `<script>` only applies to the entrypoint module). This isn't introduced here because it's not relevant to specifier resolution. See [Integrity metadata map](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#integrity_metadata_map)
.

### [Feature detection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#feature_detection)

You can check support for import maps using the [`HTMLScriptElement.supports()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement/supports_static)
 static method (which is itself broadly supported):

### [The `imports` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#the_imports_object)

The `imports` property contains an object where each property value is a string. Other data types used as values will become `null`. There are many other conditions, introduced below, that will also cause the value to become `null`. When the resolver hits an entry whose value is `null`, the resolution for that specifier immediately fails.

Each key must be one of two kinds:

*   The key does not end in `/`: it will be compared to the specifier as-is.
*   The key ends in `/`: it will be compared as a prefix of the specifier. In this case, the value must also end in `/`, otherwise it becomes `null`. More on prefix matching later.

The value must be a URL, resolved relative to the [base URL](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
 of the document containing the import map. If URL parsing failed, the value becomes `null`. (Note that relative URLs can be "bare"; only module specifiers aren't allowed to be bare.)

The property order of the `imports` object does not matter: internally, they are always sorted in descending lexicographic order by keys. During resolution, the properties are matched in order.

#### Literal matching

Suppose the following `<script>` element is included in the page at `https://example.com/welcome`.

Here, we use a relative URL as the value, which is resolved relative to the document's base URL, so it's equivalent to writing `https://example.com/welcome/shapes/square.js`. Had this `<script>` element been contained in the page `https://example.com/welcome/`, the value would be equivalent to `https://example.com/welcome/shapes/square.js` instead.

Now when the specifier resolver encounters a specifier like the following:

It will go through the `imports` entries one-by-one (of which there's only one), see that the `"square"` key is equal to the requested specifier, and use its value. The module at `https://example.com/shapes/square.js` will now be requested.

#### Prefix matching

If the key has a trailing slash `/` (in which case the value also needs a trailing slash), then in addition to literal matching, it can be matched as a prefix.

For example, consider the following import map:

Again, the relative URL value is resolved at the time the import map is parsed, relative to the document URL, so it's equivalent to writing `https://example.com/shapes/`.

Now when the specifier resolver encounters a specifier like the following:

It will go through the `imports` entries one-by-one (of which there's only one), see that the `"shapes/"` key is a prefix of the requested specifier, and use its mapped value. The key prefix is stripped from the specifier, leaving `square.js`. This remainder is resolved using the mapped value (`https://example.com/shapes/`) as the base URL. The module at `https://example.com/shapes/square.js` will now be requested.

The remainder of the specifier is not allowed to "escape" the mapped value. For example, if you write the following:

Then the remainder is `../square.js`, which when resolved relative to `https://example.com/shapes/` will give `https://example.com/square.js`. The mapped value is no longer a prefix of the final URL. The resolver will throw an error in this case.

Keys ending in `/` can still be matched literally. For example:

The resolver will resolve this to `https://example.com/shapes/` and request that URL.

Once again, the entries of the `imports` object is always sorted such that if key A is a prefix of key B, then B comes before A, so with the following import map:

The module specifier `shapes/square/index.js` will still match the more-specific `shapes/square/` in priority to `shapes/`.

#### Mixing literal matching and prefix matching

In Node, you can import either a package itself, which imports the [`main`](https://docs.npmjs.com/cli/configuring-npm/package-json#main "External link (opens in new tab)")
 file, or a file inside the package (assuming the package.json has no [`exports`](https://docs.npmjs.com/cli/configuring-npm/package-json#exports "External link (opens in new tab)")
 field):

In this case, you must provide separate entries for `lodash` and the `lodash/` prefix:

#### General URL remapping

The key does not need to be a bare name. It can also be an absolute or relative URL. Given the following import map:

Now when the specifier resolver encounters a specifier like the following:

It will use the corresponding prefix entry and resolve this to `https://example.com/node_modules/lodash-es/fp.js`. This is especially useful for testing because you can mock a module with an alternative version.

URL remapping is also helpful for removing hashes from the module name. Script files used by websites often have hashed filenames to simplify caching. The downside of this approach is that if a module changes, any modules that import it using its hashed filename will also need to be updated/regenerated. This potentially results in a cascade of updates, which is wasteful of network resources.

Import maps provide a convenient solution to this problem. Rather than depending on specific hashed filenames, applications and scripts instead depend on an un-hashed version of the module name. An import map like the one below then provides a mapping to the actual script file.

If `dependency.js` changes, then its hash contained in the file name changes as well. In this case, we only need to update the import map to reflect the changed name of the module. The JavaScript source code continues to import from `"/node/srcs/dependency.js"`.

Unfortunately, import maps don't provide "suffix matching", so you can't say something like "replace `application.js` with `application-fg7744e1b.js`, whatever the path before it is". You must now always import from `/node/srcs/application.js` instead of `./application.js`, `https://example.com/node/srcs/application.js`, etc. Ultimately, you may still find that using a bundler to compile the code and rewrite the imports to be more convenient.

### [The `scopes` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#the_scopes_object)

The `imports` object is global: the remapping is applied to all modules in the application, regardless of where they live. The same `lodash` specifier always resolves to the same module.

In real life, different modules may want to import different versions of the `lodash` package. For example, package A may depend on `lodash` v3, while package B may depend on `lodash` v4. In Node, this is achieved by giving each package its own `node_modules`:

https://example.com
└── node\_modules
    ├── lodash          <-- v4; your application and package B will use this
    ├── package-a
    │   └── node\_modules
    │       └── lodash  <-- v3; package A will use this
    └── package-b

To directly deploy this `node_modules` to your website without rewriting its source code, you must write the import map such that modules within `package-a` will have their `lodash` specifier resolve to a different address from `package-b`. You implement this with the `scopes` object, like the following:

Within the `scopes` object, each key is a scope, and each value is a module specifier map, just like `imports`. Just like keys of `imports`:

*   The scope can either not end in `/`, in which case it's matched literally against the importer's URL, or it can end in `/`, in which case it can additionally match as a prefix of the importer's URL.
*   The scope keys are sorted in descending lexicographic order (after URL resolution), so more specific prefixes match in priority to less specific ones.

The only difference is that scopes must be valid URLs which are resolved relative to the document base URL.

The scopes are attempted in order: if a scope doesn't provide the corresponding import mapping for the requested specifier, the resolver moves to the next matching scope, if any. If no scope key matches the importer, or if all matching scopes don't provide the import mapping, then the global `imports` map is used. However, if it does hit an entry anywhere in this process, but the value is `null` (e.g., if the value isn't a valid URL), resolution fails immediately without falling back.

So for example, in the example above, the scope key is `/node_modules/package-a/`, which is resolved to `https://example/node_modules/package-a/`. If the module at `https://example.com/node_modules/package-a/index.js` contains:

The resolver will look at the `scopes` in priority, see that the importer's URL is a prefix of the scope key, and use its specifier map, which defines that `lodash` should map to `https://example.com/node_modules/package-a/lodash/lodash.js`, the v3 version.

On the other hand, if the module at `https://example.com/node_modules/package-b/index.js` contains the same line, then the resolver will check `scopes` and find no matching key, and fall back to the global `imports` map, which imports `https://example.com/node_modules/lodash/lodash.js`, the v4 version.

Note that the scope key is only used to match the importer's URL; it does not provide the base URL for resolving or validating any other URL. The final mapped URL does not have to match the scope path, and relative mapped URLs are still resolved to the base URL of the script that contains the import map.

[Loading non-JavaScript resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#loading_non-javascript_resources)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#importing_json_modules)
 guide already introduces the [import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
 syntax, which allows you to import non-JavaScript resources. The resource types specified by the core language are `type: "json"` and `type: "text"`.

On the web, there is additionally `type: "css"`, which imports CSS files as [`CSSStyleSheet`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet)
 objects.

While the core language spec does not say much about the `type` attribute in general (other than how `type: "json"` must result in a JSON module and `type: "text"` must result in a text module), the HTML spec requires browsers to implement strict module type checking for security reasons. If you specify `type: "json"` or `type: "css"`, the result must be served with the corresponding `Content-Type` (such as `application/json` or `text/css`). If you don't specify any type, the result also must be served as JavaScript or WebAssembly (`text/javascript` or `application/wasm`).

In the example above with `type: "css"`, if this file turns out to be JavaScript (it is served with a `Content-Type` of `text/javascript`), the import will fail. This makes sure that you don't accidentally execute code where you don't intend to. Read the [import attribute](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
 reference for more information.

Other environments, including Node.js and Deno, often mimic web semantics, so they also require strict type matching.

On the web, the `type` attribute also changes the request's [destination](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Dest)
, so even with the same string specifier, you may end up with different module content.

[Module caching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#module_caching)

--------------------------------------------------------------------------------------------------------------------------

[Module caching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#module_caching)
 lets imports reuse a module and its state. On the web, the HTML specification defines which requests share a module.

In browsers, the [module map](https://html.spec.whatwg.org/multipage/webappapis.html#module-map "External link (opens in new tab)")
 uses the resolved request URL and the module type as its key. Different specifier strings can therefore identify the same module. For example, although the following two requests use different string specifiers, they point to the same module (assuming there's no import map that changes the resolution):

The module type, selected through [import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
, is also part of the key, so requesting a URL with `{ type: "json" }` does not reuse the entry for that URL without a `type` (which is implicitly JavaScript). Separate documents and workers have separate module maps, so importing a module in a page and in its worker does not share the module's variables between them.

Module caching is separate from [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
. HTTP caching can reuse response bytes; module caching reuses the module's identity and state. A new document can evaluate a module again even if its source comes from the HTTP cache. Conversely, `Cache-Control: no-store` does not make an already evaluated module execute again on each import.

Browsers treat URLs with different query strings or fragments as different module identities, even if they retrieve identical source code:

This creates two module instances from the same source code. Any further dependencies are still shared—if both instances import `"./logger.js"`, that specifier still resolves to the same URL from both, so they share `logger.js`.

For [loading errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#errors_from_loading)
, the [HTML specification](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-single-module-script "External link (opens in new tab)")
 requires failed fetches, including HTTP error responses, to be removed from the module map so a later import can retry. The HTTP cache may still supply a cached error response. Parse errors, however, are retained in the module map, so retrying the same module does not fetch corrected source.

[The import.meta object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#the_import.meta_object)

------------------------------------------------------------------------------------------------------------------------------------------

The [Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#module_metadata)
 guide also introduced the [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
 object and mentioned that _all_ of its properties are host-defined.

Use [`import.meta.url`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
 with the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL "URL()")
 constructor when a resource is located relative to your module:

In a window, a relative URL passed directly to `fetch()`, such as `fetch("../api/set-user")`, is resolved against the document's base URL. It is not resolved relative to the JavaScript module containing the call. Constructing the URL explicitly makes the resource location independent of the page that imports the module.

To resolve a module specifier using the host's module resolution rules, use [`import.meta.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve)
. For example, in a browser with an import map that defines `"shapes"`, `import.meta.resolve("shapes")` returns its resolved URL. Unlike `import()`, this resolves the specifier without loading or evaluating the module.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#see_also)

--------------------------------------------------------------------------------------------------------------

*   [HTML `<script>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<script type="importmap">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
    
*   [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/modules/modules_on_the_web/index.md?plain=1 "Folder: en-us/web/javascript/guide/modules/modules_on_the_web (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules%2FModules_on_the_web&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fmodules%2Fmodules_on_the_web%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules%2FModules_on_the_web%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fmodules%2Fmodules_on_the_web%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")