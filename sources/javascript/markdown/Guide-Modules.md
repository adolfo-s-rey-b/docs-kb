*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#mdn-search)
    

JavaScript modules
==================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
    

This guide gives you all you need to get started with JavaScript module syntax.

[Module philosophy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#module_philosophy)

-------------------------------------------------------------------------------------------------------------

Before we look at what syntax is available inside modules, let's first talk at a high level about what modules are, how they differ from traditional scripts, and why you might need them.

### [A background on modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#a_background_on_modules)

JavaScript programs started off pretty small — most of its usage in the early days was to do isolated scripting tasks, providing a bit of interactivity to your web pages where needed, so large scripts were generally not needed. Fast forward a few years and we now have complete applications being run in browsers with a lot of JavaScript, as well as JavaScript being used in other contexts ([Node.js](https://developer.mozilla.org/en-US/docs/Glossary/Node.js)
, for example).

Complex projects necessitate a mechanism for splitting JavaScript programs into separate modules: units of code that can be imported when needed. Node.js has had this ability for a long time, and there are a number of JavaScript libraries and tools that enable module usage (for example, [AMD](https://github.com/amdjs/amdjs-api/blob/master/AMD.md "External link (opens in new tab)")
 loaders like [RequireJS](https://requirejs.org/ "External link (opens in new tab)")
, bundlers like [Webpack](https://webpack.js.org/ "External link (opens in new tab)")
, and compilers like [Babel](https://babeljs.io/ "External link (opens in new tab)")
).

All modern browsers support module features natively without needing transpilation. It can only be a good thing — browsers can automatically handle the module loading process, without requiring a library. It does not obsolete bundlers like Webpack, though — bundlers still do a good job at partitioning code into reasonably sized chunks, and are able to do other optimizations like minification, dead code elimination, and [tree shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)
.

### [What's a module?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#whats_a_module)

JavaScript code can be evaluated in two ways: as a _script_ (also called "classic script" or "traditional script") or as a _module_. There are two main differences:

1.  At parsing time, modules are parsed with a slightly different syntax. Namely, they are automatically in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    , and you can only use [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
     and [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
     statements in modules.
2.  At runtime, modules are executed in their own scope, not in the global scope. This means that variables, functions, classes, etc. declared in a module are not visible outside the module unless they are either explicitly exported (so they can be imported in other modules), or are made available globally by attaching them to the global object (e.g., `window` in a browser). Uncaught errors from modules still show in the DevTools, but you won't be able to access module-scoped variables in the JavaScript console.

There are other differences, but they are specific to modules on the web. Find them in [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web)
.

Here is how scripts are traditionally attached to web pages:

![Diagram showing how scripts are attached to web pages](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/script-loading.svg)

Most notably, all classic scripts attached to the webpage are executed under the same scope—the global scope. Any variables, unless they are contained within other functions or blocks, can be accessed from anywhere later in the page. This can be both convenient and dangerous. Shown in this figure is how the second and third scripts are able to access the `$` variable declared in the first script, thanks to them all being in the global scope.

This pattern is very convenient, but it gets unwieldy at scale:

*   Scope pollution and identifier conflicts become a big concern. Popular libraries like [jQuery](https://jquery.com/ "External link (opens in new tab)")
     and [Underscore](https://underscorejs.org/ "External link (opens in new tab)")
     put everything under special identifiers like `$` and `_` to minimize the risk, but many third-party libraries compete for common names like `map`, `merge`, `debounce`, etc.
*   All dependencies must be explicitly declared and managed by the author. If library A imports library B, then it's the application author's job to add a `<script>` element that loads library B and ensure that it happens before A.
*   It's hard to load libraries on demand: everything is loaded and initialized as soon as the page loads.

Now, let us consider how this same code may look with modules. The first script, `external-script.js`, wants to share the variable `$` with the rest of the scripts. It is done above by putting the variable in the global scope. In the module version, we can export the variable and import it in the other scripts.

![Diagram showing how modules are attached to web pages](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/module-loading.svg)

Whereas the script version formed a _linear_ order of dependencies where each piece of code has access to all of the code coming earlier, the module version forms a [_dependency graph_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
 where each module explicitly declares the modules it relies on, and what variables it needs from those dependencies.

As we said, modules are parsed differently from scripts—this means that the JavaScript engine needs to know whether to apply the module or script parsing rules. Hosts commonly specify this using an [_out-of-band signaling mechanism_](https://github.com/tc39/how-we-work/blob/main/terminology.md#out-of-band "External link (opens in new tab)")
, where the behavior of the code is configured by information outside of the code itself. (This is different from [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, where the interpretation mode is declared inside the script with `"use strict"`.) There are many ways to give such information:

*   If this module is referenced from a `<script>` tag, you can use the `type="module"` attribute. Also see [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web)
    .
*   If you are using Node.js, you can use the `.mjs` file extension, or add `"type": "module"` to the closest `package.json` file. Also see [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
    .
*   If this module is to be used as a worker, you can pass `type: "module"` when calling the [`Worker()`](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker "Worker()")
     constructor.

**Note:** Certain runtimes, like Node.js, also have implicit module type detection if there's no explicit indication, based on whether the code uses syntax like `import`/`export` that's unavailable in non-modules. Browsers don't offer this.

Modules still have access to global variables. For example, a module can use a variable declared by a classic script:

### [Aside — .mjs versus .js](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#aside_%E2%80%94_.mjs_versus_.js)

Throughout this article, we've used `.js` extensions for our module files, but in other resources you may see the `.mjs` extension used instead. [V8's documentation recommends this](https://v8.dev/features/modules#mjs "External link (opens in new tab)")
, for example. The reasons given are:

*   You can tell if a file is a module or a script directly from the file, without looking at contextual clues like the HTML tag or the package.json.
*   Outside of browsers, it's almost universally accepted as directly entering module mode, including by runtimes such as [Node.js](https://nodejs.org/api/esm.html#esm_enabling "External link (opens in new tab)")
     and build tools such as [Babel](https://babeljs.io/docs/options#sourcetype "External link (opens in new tab)")
    .

For browsers, the difference is purely cosmetic. The file extension doesn't matter on the web—JavaScript is identified by the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)
 header, and modules are identified by the `type="module"` attribute in the `<script>` tag. To get modules to work correctly in a browser, you need to make sure that your server is serving them with a `Content-Type` header that contains a JavaScript MIME type such as `text/javascript`. If you don't, you'll get a strict MIME type checking error along the lines of "The server responded with a non-JavaScript MIME type" and the browser won't run your JavaScript.

We decided to keep to `.js`. The main benefit is that the `.js` extension is much more widely understood than `.mjs`, and although the latter is catching up, you might always run into certain software that doesn't understand `.mjs`.

*   Most servers automatically set the correct type for `.js` files, but some don't for `.mjs` files. Servers that already serve `.mjs` files correctly include [GitHub Pages](https://pages.github.com/ "External link (opens in new tab)")
     and [`http-server`](https://github.com/http-party/http-server#readme "External link (opens in new tab)")
     for Node.js. This is OK if you are using such an environment already, or if you aren't but you have access to configure your server to set the correct `Content-Type` for `.mjs` files. It could however cause confusion if you don't control the server you are serving files from, or are publishing files for public use, as we are here.
*   The file extension is used by many tools other than the HTTP server. It may be used by your editor, the operating system, static analysis tools, formatters, and more. `.mjs` may be less well-supported by tooling at large. For example, some operating systems might not recognize it, or try to replace it with something else, such as implicitly appending a `.js` extension when you try to open it.

If you really value the clarity of using `.mjs` for modules versus using `.js` for "normal" JavaScript files, but don't want to run into the problem described above, you could always use `.mjs` during development and convert them to `.js` during your build step.

[Working with examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#working_with_examples)

---------------------------------------------------------------------------------------------------------------------

To demonstrate usage of modules, we've created a [simple set of examples](https://github.com/mdn/js-examples/tree/main/module-examples "External link (opens in new tab)")
 that you can find on GitHub. These examples demonstrate a simple set of modules that create a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element on a webpage, and then draw (and report information about) different shapes on the canvas.

These are fairly trivial, but have been kept deliberately simple to demonstrate modules clearly.

In our first example (see [basic-modules](https://github.com/mdn/js-examples/tree/main/module-examples/basic-modules "External link (opens in new tab)")
) we have a file structure as follows:

index.html
main.js
modules/
    canvas.js
    square.js

**Note:** All of the examples in this guide have essentially this same structure.

The `index.html` file only declares the DOM and [applies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#applying_modules_to_your_html)
 the `main.js` module; all code we demonstrate subsequently concerns only the `.js` files.

The `modules` directory's two modules are described below:

*   `canvas.js` — contains functions related to setting up the canvas:
    *   `create()` — creates a canvas with a specified `width` and `height` inside a wrapper [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
         with a specified ID, which is itself appended inside a specified parent element. Returns an object containing the canvas's 2D context and the wrapper's ID.
    *   `createReportList()` — creates an unordered list appended inside a specified wrapper element, which can be used to output report data into. Returns the list's ID.
*   `square.js` — contains:
    *   `name` — a constant containing the string 'square'.
    *   `draw()` — draws a square on a specified canvas, with a specified size, position, and color. Returns an object containing the square's size, position, and color.
    *   `reportArea()` — writes a square's area to a specific report list, given its length.
    *   `reportPerimeter()` — writes a square's perimeter to a specific report list, given its length.

After you've downloaded these examples, [start a local server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/set_up_a_local_testing_server)
 and visit the `index.html` file.

[Named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#named_exports)

-----------------------------------------------------------------------------------------------------

Unlike scripts, where all variables declared at the top level are implicitly accessible to subsequent scripts, you must explicitly [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
 variables for them to be accessible in other modules. You can place this keyword in front of any [declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
—including `var`, `let`, `const`, `function`, `class`, and more. They need to be top-level items: for example, you can't use `export` inside a function.

Equivalently, you can export things you already declared elsewhere inside this module by using `export` followed by a comma-separated list of variable names within curly braces:

[Named imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#named_imports)

-----------------------------------------------------------------------------------------------------

Once you've exported some variables out of your module, you need to import them into another module to use them. You use the [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 statement, followed by a comma-separated list of the names you want to import wrapped in curly braces, followed by the keyword `from`, followed by the _module specifier_.

You can see such lines in action in [`main.js`](https://github.com/mdn/js-examples/blob/main/module-examples/basic-modules/main.js "External link (opens in new tab)")
.

**Note:** The _module specifier_ is a string that points to the module that exports these variables. In a browser, this is usually the URL relative to the URL of the current module, similar to the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute of [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements. For example, if our module above is served at `https://example.com/basic-modules/main.js`, and the `square.js` module is served at `https://example.com/basic-modules/modules/square.js`, then all of the following are equivalent:

"https://example.com/basic-modules/modules/square.js"
"/basic-modules/modules/square.js"
"./modules/square.js"

Different runtimes (browsers, Node, bundler, etc.) have different rules for the specifier format. You can read more about these differences in [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#module_specifiers_on_the_web)
 and [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
.

Once you've imported the features into your script, you can use them just like they were defined inside the same file. The following is found in `main.js`, below the import lines:

**Note:** The imported values are read-only views of the features that were exported. Similar to `const` variables, you cannot re-assign the variable that was imported, but you can still modify properties of object values. The value can only be re-assigned by the module exporting it. See the [`import` reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#imported_values_can_only_be_modified_by_the_exporter)
 for an example.

[Default exports and imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#default_exports_and_imports)

---------------------------------------------------------------------------------------------------------------------------------

The examples above export and import variables by name. The names for each variable have to match between the exporter and the importer. You can write functional module code using just named imports and exports. However, if you want to import from [non-ESM modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
 (like CommonJS or non-JavaScript files), these systems do not use named exports. In these systems, each module corresponds to exactly one JavaScript value. To represent these types of modules, JavaScript provides a _default export_. This has other use cases, such as modules that are built around one main value—a single class or function—where the default export lets each importer pick its own local name without knowing what the exporting module calls it.

Unlike named exports, default exports have no names associated with them. Each module can have up to one default export. To create a default export, instead of exporting a _declaration_ like `const` or `function`, you export an _expression_ instead, by prepending `export default` to it. For example, all of the following would work:

You can see the last version in our basic-modules `square.js`, which exports a function called `randomSquare()` that creates a square with a random color, size, and position. Note the lack of curly braces.

As a special case, functions and classes are exported as _declarations_, not expressions, and these declarations can be anonymous. So you can also default-export a function directly when you declare it:

Again, note the lack of curly braces. This is because there is only one default export allowed per module, and we know that `randomSquare` is it. You can name this import however you want—it doesn't have to match the function name on the exporting side.

Named exports and default export can coexist in the same module.

[Avoiding naming conflicts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#avoiding_naming_conflicts)

-----------------------------------------------------------------------------------------------------------------------------

So far, our canvas shape drawing modules seem to be working OK. But what happens if we try to add a module that deals with drawing another shape, like a circle or triangle? These shapes would probably have associated functions like `draw()`, `reportArea()`, etc. too; if we tried to import different functions of the same name into the same top-level module file, we'd end up with conflicts and errors.

Let's look at a real example. In our [renaming](https://github.com/mdn/js-examples/tree/main/module-examples/renaming "External link (opens in new tab)")
 directory you'll see the same module system as in the previous example, except that we've added `circle.js` and `triangle.js` modules to draw and report on circles and triangles.

Inside each of these modules, we've got features with the same names being exported, and therefore each has the same `export` statement at the bottom:

When importing these into `main.js`, if we tried to use

The browser would throw an error such as "SyntaxError: redeclaration of import name" (Firefox).

Fortunately there are a number of ways to get around this. We'll look at these in the following sections.

### [Renaming imports and exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#renaming_imports_and_exports)

Inside your `import` and `export` statement's curly braces, you can use the keyword `as` along with a new feature name, to change the identifying name you will use for a feature inside the top-level module.

So in our renaming example, we can rename the imports so that they are unique:

Note that you could solve the problem in the module files instead, e.g.

And it would work just the same. What style you use is up to you, however it arguably makes more sense to leave your module code alone, and make the changes in the imports. This especially makes sense when you are importing from third party modules that you don't have any control over.

By the way, you can use the same syntax for default exports too, by referring to the export name `default` (this is a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
, not an actually valid identifier name). The difference with `export default randomSquare;` is that this exports the existing _live binding_, instead of capturing the value of the expression. If you re-assign `randomSquare` in the exporter, this form allows the importer to see the new value. Named default function and class declarations, such as `export default function randomSquare() {}`, also export live bindings.

### [Creating a module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#creating_a_module_namespace_object)

The above method works OK, but it's a little messy and long-winded. An even better solution is to import each module's features inside a _module namespace object_. The following syntax form does that:

This grabs all the exports available inside `module.js`, and makes them available as members of an object `Module`, effectively giving it its own namespace. So for example:

Again, let's look at a real example. If you go to our [module-objects](https://github.com/mdn/js-examples/tree/main/module-examples/module-objects "External link (opens in new tab)")
 directory, you'll see the same example again, but rewritten to take advantage of this new syntax. In the modules, the exports are all in the following simple form:

The imports on the other hand look like this:

In each case, you can now access the module's imports underneath the specified object name, for example:

So you can now write the code just the same as before (as long as you include the object names where needed), and the imports are much neater.

### [Modules and classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#modules_and_classes)

As we hinted at earlier, you can also export and import classes; this is another option for avoiding conflicts in your code, and is especially useful if you've already got your module code written in an object-oriented style.

You can see an example of our shape drawing module rewritten with ES classes in our [classes](https://github.com/mdn/js-examples/tree/main/module-examples/classes "External link (opens in new tab)")
 directory. As an example, the [`square.js`](https://github.com/mdn/js-examples/blob/main/module-examples/classes/modules/square.js "External link (opens in new tab)")
 file now contains all its functionality in a single class:

which we then export:

And then use the class to draw our square:

[Aggregating modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#aggregating_modules)

-----------------------------------------------------------------------------------------------------------------

We now have multiple modules, each doing a similar thing. If someone wants to use several of these, they have to write a separate import declaration for each:

But it would be better if we could put all these exports into the same module, so no matter how many of these exports users need, they can grab all of them with one `import`.

In our [module-aggregation](https://github.com/mdn/js-examples/tree/main/module-examples/module-aggregation "External link (opens in new tab)")
 example (based on our earlier classes example) we've got an extra module called `shapes.js`, which aggregates all the functionality from `circle.js`, `square.js`, and `triangle.js` together. This is called a "barrel module" because it doesn't do anything other than aggregating exports from all other modules. We've also moved our submodules inside a subdirectory inside the `modules` directory called `shapes`. So the module structure in this example is:

modules/
  canvas.js
  shapes.js
  shapes/
    circle.js
    square.js
    triangle.js

These grab the exports from the individual submodules and effectively make them available from the `shapes.js` module. But there's no need to `import` something just to `export` it. You can use the `export ... from` syntax to directly import and re-export in one line.

**Note:** The exports referenced in `shapes.js` basically get redirected through the file and don't really exist there, so you won't be able to write any useful related code inside the same file.

Alternatively, you can replace `shapes.js` with the special `export * from` syntax:

This re-exports _all_ exports (other than the default) from the target module as named exports of the current module, so if you export something else from `square.js`, you don't have to modify `shapes.js` as well. Only do this if you actually want `shapes.js` to re-export everything from `square.js`, or you may accidentally expose things.

Almost all `import` syntaxes we've introduced have `export ... from` equivalents. The only exception is the default import `import x from "mod"`, for which `export x from "mod"` does not exist, and you must use the special `export { default } from` syntax.

[Importing a module for its side effects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#importing_a_module_for_its_side_effects)

---------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you want to run a module's initialization code without importing any of its exports, for example, to install a polyfill. Use an import with only a module specifier:

See the [`import` reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#import_a_module_for_its_side_effects_only)
 for more information.

[Import declarations are hoisted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#import_declarations_are_hoisted)

-----------------------------------------------------------------------------------------------------------------------------------------

Import declarations are [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
. In this case, it means that the imported values are available in the module's code even before the place that declares them, and that the imported module's side effects are produced before the rest of the module's code starts running.

So for example, in `main.js`, importing `Canvas` in the middle of the code would still work:

However, it is considered good practice to put all your imports at the top of the code, which makes it easier to analyze dependencies.

[Importing JSON modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#importing_json_modules)

-----------------------------------------------------------------------------------------------------------------------

We have seen how to import from JavaScript modules, where data is exported with `export` statements. You can also import values from modules written in other languages, as long as the runtime environment knows how to interpret them. The specification only defines two other resource types: JSON modules and [text modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with#text_modules_type_text)
. Here, we look at JSON modules, which are more common.

A JSON module is basically a standalone JSON file. When imported, it provides a single default export containing the parsed JSON value. You import it like this:

Notice the extra `with { type: "json" }` at the end. This is an [import attribute](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
 that tells the runtime environment to validate that the loaded file is indeed JSON. We will talk more about them in the [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#loading_non-javascript_resources)
 guide, because their semantics are not defined in the core language. You might be able to import JSON modules without `with { type: "json" }`. The only requirement is that if `with { type: "json" }` is specified, then the loaded module must be parsed as JSON. It is good practice to always declare the type of the module you are importing so it can work everywhere.

Text modules work similarly and result in strings.

[Dynamic module loading](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#dynamic_module_loading)

-----------------------------------------------------------------------------------------------------------------------

You can also dynamically load modules only when they are needed, rather than having to load everything up front. This has some obvious performance advantages; let's read on and see how it works.

The [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 operator can be called with the path to the module as a parameter. It returns a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
, which fulfills with a module namespace object (see [Creating a module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#creating_a_module_namespace_object)
) giving you access to that object's exports. For example:

**Note:** Dynamic import is permitted in the browser main thread, and in shared and dedicated workers. However `import()` will reject if called in a service worker or worklet.

Let's look at an example. In the [dynamic-module-imports](https://github.com/mdn/js-examples/tree/main/module-examples/dynamic-module-imports "External link (opens in new tab)")
 directory we've got another example based on our classes example. This time however we are not drawing anything on the canvas when the example loads. Instead, we include three buttons — "Circle", "Square", and "Triangle" — that, when pressed, dynamically load the required module and then use it to draw the associated shape.

In this example we've only made changes to our [`index.html`](https://github.com/mdn/js-examples/blob/main/module-examples/dynamic-module-imports/index.html "External link (opens in new tab)")
 and [`main.js`](https://github.com/mdn/js-examples/blob/main/module-examples/dynamic-module-imports/main.js "External link (opens in new tab)")
 files — the module exports remain the same as before.

Over in `main.js` we've grabbed a reference to each button using a [`document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
 call, for example:

We then attach an event listener to each button so that when pressed, the relevant module is dynamically loaded and used to draw the shape:

Note that, because the promise fulfillment returns a module namespace object, the class is then made a subfeature of the object, hence we now need to access the constructor with `Module.` prepended to it, e.g., `Module.Square( /* … */ )`.

Another advantage of dynamic imports is that they are always available, even in script environments. Therefore, if you have an existing `<script>` tag in your HTML that doesn't have `type="module"`, you can still reuse code distributed as modules by dynamically importing it.

[Top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#top-level_await)

---------------------------------------------------------------------------------------------------------

Top-level `await` is a feature available within modules: the `await` keyword can be used at the top level, outside any async function. It allows a module to act as a big [asynchronous function](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS/Introducing)
, meaning it can finish asynchronous work before modules that depend on it execute, without blocking the evaluation of sibling modules that don't depend on it.

Let's take a look at an example. You can find all the files and code described in this section within the [`top-level-await`](https://github.com/mdn/js-examples/tree/main/module-examples/top-level-await "External link (opens in new tab)")
 directory, which extends from the previous examples.

Firstly we'll declare our color palette in a separate [`colors.json`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/data/colors.json "External link (opens in new tab)")
 file:

Then we'll create a module called [`getColors.js`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/modules/getColors.js "External link (opens in new tab)")
 which uses a fetch request to load the [`colors.json`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/data/colors.json "External link (opens in new tab)")
 file and return the data as an object.

Notice the last export line here.

We're using the keyword `await` before specifying the constant `colors` to export. This means any other modules which include this one will wait until `colors` has been downloaded and parsed before using it.

We'll use `colors` instead of the previously used strings when calling our shape functions:

This is useful because the code within [`main.js`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/main.js "External link (opens in new tab)")
 won't execute until the code in [`getColors.js`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/modules/getColors.js "External link (opens in new tab)")
 has run. However, it doesn't hold up the evaluation of independent modules: our [`canvas.js`](https://github.com/mdn/js-examples/blob/main/module-examples/top-level-await/modules/canvas.js "External link (opens in new tab)")
 module still evaluates while `colors` is being fetched.

Top-level `await` is not free; it has deep implications because it means a part of the [module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
 can only be evaluated asynchronously. See the [module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#top-level_await_and_asynchronous_evaluation)
 guide for more information.

[Module metadata](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#module_metadata)

---------------------------------------------------------------------------------------------------------

Scripts are executed in the global context, so they can get information about their environment with global variables, such as [`Window.document`](https://developer.mozilla.org/en-US/docs/Web/API/Window/document)
 or [`Window.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)
. Each module also has its own execution context which is accessed via a module-specific [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
 object. The properties of this object are defined by the host environment; the core language spec does not define any properties. See [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#the_import.meta_object)
 for information about browsers, and [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
 for information about Node.js, bundlers, and more.

Just as an example, in most web-like environments (browsers, Node.js, bundlers, etc.), `import.meta.url` provides the module's URL, which you can use to locate a resource relative to the module:

This keeps the resource URL relative to `getColors.js` even when the module is imported from a page or module in another directory.

[Language versus host responsibilities](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#language_versus_host_responsibilities)

-----------------------------------------------------------------------------------------------------------------------------------------------------

This article introduces modules as they are defined in the ECMAScript spec. JavaScript modules are inherently tied to the host environment. They need to adapt to different I/O conditions, different architectures, and different engineering needs. As such, the core language only defines the following:

*   The syntax for module features, such as [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
     and [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
     declarations, [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
    , and the [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
     expression.
*   [Module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
     building, linking, and evaluation, including cycle detection.
*   The [module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#creating_a_module_namespace_object)
    's shape.

The core language does _not_ care about the following:

*   The concept of "files". Although each module is conventionally a separate file, it could as well be an in-memory object, a dynamically fetched string, or anything that can be represented as a JavaScript value.
*   The structure of the module specifier string. It could be a URL, a file path, or any other identifier the host recognizes.
*   The properties of `import.meta`. All properties, including `import.meta.url`, are host-defined.
*   The module loading process. The host environment is responsible for fetching modules, including applying any [import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
    , subject to the language's requirements, such as those for JSON modules.

In reality, runtime environments like browsers, Node.js, and Deno often end up implementing the same set of features, so that code is more likely to work across platforms. This guide walks through an example that's run in the browser, but we focus on core concepts that are applicable to all environments. In the [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web)
 guide, we'll cover the specifics of module loading in browsers, especially import specifiers. Then, in the [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
 guide, we will go further and discuss how the module system is integrated with other environments.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#see_also)

-------------------------------------------------------------------------------------------

*   [Using modules on the web](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web)
    
*   [Understanding the module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
    
*   [Modules across platforms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_across_platforms)
    
*   [JavaScript modules](https://v8.dev/features/modules "External link (opens in new tab)")
     on v8.dev (2018)
*   [ES modules: A cartoon deep-dive](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/ "External link (opens in new tab)")
     on hacks.mozilla.org (2018)
*   [ES6 in Depth: Modules](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)
*   [Exploring JS, Ch.16: Modules](https://exploringjs.com/es6/ch_modules.html "External link (opens in new tab)")
     by Dr. Axel Rauschmayer

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/modules/index.md?plain=1 "Folder: en-us/web/javascript/guide/modules (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fmodules%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fmodules%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")