*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#mdn-search)
    

`<script type="importmap">` HTML attribute value
================================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`importmap`** value of the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type)
 attribute of the [`<script>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 indicates that the body of the element contains an import map.

An import map is a JSON object that allows developers to control how the browser resolves module specifiers when importing [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
. It provides a mapping between the text used as the module specifier in an [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 or [`import()` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
, and the corresponding value that will replace the text when resolving the specifier. The JSON object must conform to the [Import map JSON representation format](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#import_map_json_representation)
.

An import map is used to resolve module specifiers in static and dynamic imports, and therefore must be declared and processed before any `<script>` elements that import modules using specifiers declared in the map. Note that the import map applies only to module specifiers in the [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 or [`import()` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 for modules loaded into documents; it does not apply to the path specified in the `src` attribute of a `<script>` element or to modules loaded into workers or worklets.

For more information, see the [Importing modules using import maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)
 section in the Using modules on the web guide.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#syntax)

------------------------------------------------------------------------------------------------------------

The `src`, `async`, `nomodule`, `defer`, `crossorigin`, `integrity`, and `referrerpolicy` attributes must not be specified.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

The import map definition is not a JSON object, the `importmap` key is defined but its value is not a JSON object, or the `scopes` key is defined but its value is not a JSON object.

Browsers generate console warnings for other cases where the import map JSON does not conform to the [import map](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#import_map_json_representation)
 schema.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#description)

----------------------------------------------------------------------------------------------------------------------

When importing a [JavaScript module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
, both the [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 and [`import()` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 have a "module specifier" that indicates the module to be imported. A browser must be able to resolve this specifier to an absolute URL in order to import the module.

For example, the following statements import elements from the module specifier `"https://example.com/shapes/circle.js"`, which is an absolute URL, and the module specifier `"./modules/shapes/square.js"`, which is a path relative to the base URL of the document.

Import maps allow developers to specify (almost) any text they want in the module specifier; the map provides a corresponding value that will replace the text when the module specifier is resolved.

### [Bare modules](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#bare_modules)

The import map below defines an `imports` key that has a "module specifier map" with properties `circle` and `square`.

With this import map we can import the same modules as above, but using "bare modules" in our module specifiers:

### [Mapping path prefixes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#mapping_path_prefixes)

A module specifier map key can also be used to remap a path prefix in a module specifier. Note that in this case the property and mapped path must both have a trailing forward slash (`/`).

We could then import a circle module as shown.

### [Paths in the module specifier map key](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#paths_in_the_module_specifier_map_key)

Module specifier keys do not have to be single word names ("bare names"). They can also contain or end with path separators, or be absolute URLs, or be relative URL paths that start with `/`, `./`, or `../`.

If there are several module specifier keys in a module specifier map that might match, then the most specific key will be selected (i.e., the one with the longer path/value).

A module specifier of `./foo/../js/app.js` would be resolved to `./js/app.js` before matching. This means that a module specifier key of `./js/app.js` would match the module specifier even though they are not exactly the same.

### [Scoped module specifier maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#scoped_module_specifier_maps)

You can use the `scopes` key to provide mappings that are only used if the script importing the module contains a particular URL path. If the URL of the loading script matches the supplied path, the mapping associated with the scope will be used. This allows different versions of the module to be used depending on what code is doing the importing.

For example, the map below will only use the scoped map if the loading module has a URL that includes the path: "/modules/custom-shapes/".

If multiple scopes match the referrer URL, then the most specific scope path is used (the scope key name with the longest name). The browser falls back to the next most specific scoped path if there is no matching specifier, and so on, eventually falling back to the module specifier map in the `imports` key.

### [Integrity metadata map](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#integrity_metadata_map)

You can use the `integrity` key to provide mapping for module [integrity metadata](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity#using_subresource_integrity)
. This enables you to ensure the integrity of dynamically or statically imported modules. `integrity` also enables you to provide a fallback for top-level or preloaded modules, in case they don't already include an `integrity` attribute.

The map keys represent module URLs, which can be absolute or relative (starting with `/`, `./`, or `../`). The map values represent integrity metadata, identical to that used in [`integrity`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#integrity)
 attribute values.

For example, the map below defines integrity metadata for the `square.js` module (directly) and its bare specifier (transitively, via the `imports` key).

### [Merging multiple import maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#merging_multiple_import_maps)

Supporting browsers can declare one or more import maps anywhere in the document, provided they are defined before any module that depends on them is loaded (some [browser versions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility)
 allow only a single import map declaration, which must appear before any module is loaded).

Internally, browsers maintain a single global import map representation. When multiple import maps are included in a document, their contents are merged into the global import map when they are registered.

For example, consider the following two import maps:

These are equivalent to the following single import map:

Module specifiers in each registered map that were already resolved beforehand are dropped. Subsequent resolutions of these specifiers will provide the same results as their previous resolutions.

For example, if the module specifier `/app/helper.js` was already resolved, the following new import map:

Would be equivalent to:

The `/app/helper.js` rule was ignored and not incorporated into the map.

Similarly, module specifiers in a registered map that were already mapped to URLs in the global map are dropped; their previous mapping prevails.

For example, the following two import maps:

Are equivalent to the following single import map:

The `/app/helper/` rule was dropped from the second map.

**Note:** In non-supporting browsers (check the [compatibility data](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility)
), a [polyfill](https://github.com/guybedford/es-module-shims "External link (opens in new tab)")
 can be used to avoid issues related to module resolution.

[Import map JSON representation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#import_map_json_representation)

------------------------------------------------------------------------------------------------------------------------------------------------------------

The following is a "formal" definition of the import map JSON representation.

The import map must be a valid JSON object that can define any of the optional keys `imports`, `scopes` and `integrity`. Each key's value must be an object, which may be empty.

[`imports` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#imports)

The value is a [module specifier map](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#module_specifier_map)
, which provides the mappings between module specifier text that might appear in an `import` statement or `import()` operator, and the text that will replace it when the specifier is resolved.

This is the fallback map that is searched for matching module specifiers if no `scopes` path URLs match, or if module specifier maps in matching `scopes` paths do not contain a key that matches the module specifier.

[`<module specifier map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#module_specifier_map)

A "module specifier map" is a valid JSON object where the _keys_ are text that may be present in the module specifier when importing a module, and the corresponding _values_ are the URLs or paths that will replace this text when the module specifier is resolved to an address.

The module specifier map JSON object has the following requirements:

*   None of the keys may be empty.
*   All of the values must be strings, defining either a valid absolute URL or a valid URL string that starts with `/`, `./`, or `../`.
*   If a key ends with `/`, then the corresponding value must also end with `/`. A key with a trailing `/` can be used as a prefix for when mapping (or remapping) modules addresses.
*   The object properties' ordering is irrelevant: if multiple keys can match the module specifier, the most specific key is used (in other words, a specifier "olive/branch/" would match before "olive/").

[`integrity` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#integrity)

Defines a valid JSON object where the _keys_ are strings containing valid absolute or relative URLs (starting with `/`, `./`, or `../`), and the corresponding _values_ are valid [integrity metadata](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity#using_subresource_integrity)
.

If the URL of a script importing or preloading a module matches a key in the `integrity` object, the corresponding integrity metadata is applied to the script's fetch options, unless they already have integrity metadata attached to them.

[`scopes` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#scopes)

Scopes define path-specific [module specifier maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#module_specifier_map)
, allowing the choice of map to depend on the path of the code importing the module.

The scopes object is a valid JSON object where each property is a `<scope key>`, which is a URL path, with a corresponding value that is a `<module specifier map>`.

If the URL of a script importing a module matches a `<scope key>` path, then the `<module specifier map>` value associated with the key is checked for matching specifiers first. If there are multiple matching scope keys, then the value associated with the most specific/nested scope paths are checked for matching module specifiers first. The fallback module specifier map in `imports` is used if there are no matching module specifier keys in any of the matching scoped module specifier maps.

Note that the scope does not change how an address is resolved; relative addresses are always resolved to the import map base URL.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# import-map](https://html.spec.whatwg.org/multipage/webappapis.html#import-map) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Using modules on the web > Importing modules using import maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)
    
*   [The `type` attribute of HTML `<script>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type)
    
*   [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`import()` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/script/type/importmap/index.md?plain=1 "Folder: en-us/web/html/reference/elements/script/type/importmap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype%2Fimportmap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%2Fimportmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype%2Fimportmap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%2Fimportmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")