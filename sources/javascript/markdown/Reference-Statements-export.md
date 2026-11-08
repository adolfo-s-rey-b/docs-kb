*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#mdn-search)
    

export
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since May 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`export`** declaration is used to export values from a JavaScript module. Exported values can then be imported into other programs with the [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declaration or [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
. The value of an imported binding is subject to change in the module that exports it — when a module updates the value of a binding that it exports, the update will be visible in its imported value.

In order to use the `export` declaration in a source file, the file must be interpreted by the runtime as a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
. In HTML, this is done by adding `type="module"` to the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 tag, or by being imported by another module. Modules are automatically interpreted in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#syntax)

-----------------------------------------------------------------------------------------------------

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#namen)

Identifier to be exported (so that it can be imported via [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 in another script). If you use an alias with `as`, the actual exported name can be specified as a string literal, which may not be a valid identifier.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#description)

---------------------------------------------------------------------------------------------------------------

Every module can have two different types of export, _named export_ and _default export_. You can have multiple named exports per module but only one default export. Each type corresponds to one of the above syntax.

Named exports:

After the `export` keyword, you can use `let`, `const`, and `var` declarations, as well as function or class declarations. You can also use the `export { name1, name2 }` syntax to export a list of names declared elsewhere. Note that `export {}` does not export an empty object — it's a no-op declaration that exports nothing (an empty name list).

You cannot use `export` on a [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 or [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
 declaration. You can, however, export a variable that was declared elsewhere using `using` or `await using`. Doing so is still strongly discouraged, because the variable is disposed as soon as the module finishes executing, causing all importers to receive a value that's already disposed.

Export declarations are not subject to [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
 rules. You can declare that the module exports `X` before the name `X` itself is declared.

Default exports:

`export { myFunction as default }` exports a live binding, whereas `export default myFunction` evaluates `myFunction` and exports its value at that point. Later reassignment of `myFunction` only updates the default export in the first form.

**Note:** Names for export declarations must be distinct from each other. Having exports with duplicate names or using more than one `default` export will result in a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 and prevent the module from being [evaluated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#evaluating_modules)
.

The `export default` syntax allows any expression.

As a special case, functions and classes are exported as _declarations_, not expressions, and these declarations can be anonymous. This means functions will be hoisted.

Named exports are useful when you need to export several values. When importing this module, named exports must be referred to by the exact same name (optionally renaming it with `as`), but the default export can be imported with any name. For example:

You can also rename named exports to avoid naming conflicts:

You can rename a name to something that's not a valid identifier by using a string literal. For example:

### [Re-exporting / Aggregating](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#re-exporting_aggregating)

A module can also "relay" values exported from other modules without the hassle of writing two separate import/export statements. This is often useful when creating a single module concentrating various exports from various modules (usually called a "barrel module").

This can be achieved with the "export from" syntax:

Which is comparable to a combination of import and export, except that `function1` and `function2` do not become available inside the current module:

Most of the "import from" syntaxes have "export from" counterparts.

There is also `export * from "mod"`, although there's no `import * from "mod"`. This re-exports all **named** exports from `mod` as the named exports of the current module, but the default export of `mod` is not re-exported. If two wildcard export statements implicitly re-export the same name from different bindings, the name is ambiguous and is omitted from the module namespace. If both resolve to the same binding, there is no ambiguity. An explicit export of that name takes precedence over wildcard exports.

Attempting to import the ambiguous name directly will throw a syntax error during [linking](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#linking_modules)
, before evaluation starts.

The following is syntactically invalid despite its import equivalent:

**Note:** Due to the lack of this syntax, [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
 also has no re-exporting counterpart.

The correct way of doing this is to rename the export:

The "export from" syntax allows the `as` token to be omitted, which makes the default export still re-exported as default export.

`export from` supports all features that `import` supports — for example, [import attributes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with)
:

**Note:** The [`import defer * as ns`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)
 declaration has no re-exporting counterpart, despite `import * as ns` having one. Deferred re-exports are being developed in a [separate proposal](https://github.com/tc39/proposal-deferred-reexports "External link (opens in new tab)")
, because they can also avoid [loading](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 unused modules, which requires additional tree-shaking semantics. You can instead [import and export in two separate statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer#exporting_a_deferred_namespace)
, although this immediately loads the module.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#examples)

---------------------------------------------------------------------------------------------------------

### [Using named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#using_named_exports)

Then in the top-level module included in your HTML page, we could have:

It is important to note the following:

*   You need to include this script in your HTML with a [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
     element of `type="module"`, so that it gets recognized as a module and dealt with appropriately.
*   You can't run JS modules via a `file://` URL — you'll get [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
     errors. You need to run it via an HTTP server.

### [Using the default export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#using_the_default_export)

If we want to export a single value representing an entire module, we could use a default export:

Then, in another script, it is straightforward to import the default export:

### [Using export from](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#using_export_from)

Let's take an example where we have the following hierarchy:

*   `childModule1.js`: exporting `myFunction` and `myVariable`
*   `childModule2.js`: exporting `MyClass`
*   `parentModule.js`: acting as an aggregator (and doing nothing else)
*   top level module: consuming the exports of `parentModule.js`

This is what it would look like using code snippets:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-exports](https://tc39.es/ecma262/multipage/ecmascript-language-scripts-and-modules.html#sec-exports) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export#see_also)

---------------------------------------------------------------------------------------------------------

*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
     guide
*   [ES6 in Depth: Modules](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)
*   [ES modules: A cartoon deep-dive](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/ "External link (opens in new tab)")
     on hacks.mozilla.org (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/export/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/export (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fexport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fexport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fexport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fexport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")