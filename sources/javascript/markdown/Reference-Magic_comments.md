*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#mdn-search)
    

Magic comments
==============

**Magic comments** (also called **comment directives**, **annotations**, etc.) are special types of [comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)
 that are recognized by certain engines, bundlers, type checkers, debuggers, etc. (collectively referred to as _consumers_) to enable opt-in functionality. Because they're comments, consumers that don't understand them ignore them. This article introduces the various types of magic comments commonly seen in JavaScript source code and their intended consumers.

Usually, the presence or absence of magic comments doesn't change the program's runtime behavior—for example, they may optimize execution, enable/disable static checking, or provide additional metadata. This contrasts with _directives_, which are strings that do alter runtime behavior. Examples include the standard [`"use strict"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 directive to opt into strict mode and React's [`"use server"`](https://react.dev/reference/rsc/use-server "External link (opens in new tab)")
 and [`"use client"`](https://react.dev/reference/rsc/use-client "External link (opens in new tab)")
 directives that determine if a component is executed server-side or client-side.

To avoid collision with regular comments, magic comments are usually marked by _sigils_, such as a leading `#` or `@` character: `//# my-setting-name` or `//@ my-setting-name`. The exact syntax varies between comment types.

**Note:** There's no universal name for this type of feature, and the "alternatives" we listed may have subtle differences: _pragmas_ are usually placed at the beginning of the file and inform compilers or engines about the entire script; _annotations_ may be placed anywhere and apply to a specific construct; _directives_ are generic terms but may be ambiguous with the JavaScript `"use strict"` style convention. In our writing, we use all these words interchangeably.

[Compile hint pragmas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#compile_hint_pragmas)

------------------------------------------------------------------------------------------------------------------------------

Compile hint pragmas give JavaScript engine hints about how to compile the code ahead-of-time. Their interpretation depends on the engine.

They are specified in the WICG proposal [Explicit JavaScript Compile Hints](https://wicg.github.io/explicit-javascript-compile-hints-file-based/ "External link (opens in new tab)")
.

### [Eager compilation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#eager_compilation)

The following pragma enables eager compilation of all functions in the current script.

The syntax and placement requirements are as follows:

*   This comment must be placed at the beginning of the script before any code or whitespace (only other comments, single-line or block, are allowed to precede it).
*   The comment can be either a line comment or a block comment.
*   There must be no space between `#` and `//` or `/*`.
*   There can be any amount of whitespace before and after `allFunctionsCalledOnLoad`.

In the following example, the magic comment indicates that the functions in the file are likely to be called during page load:

Without the hint, the engine may defer compilation of a function until it is called.

Eager compilation offers the following benefits:

*   It avoids double parsing: During initialization, the engine already does "light parsing" to know where the function starts and ends, and it has to do another full parse when the function is called. When the function can be compiled eagerly, the engine does the full parse up front, without a separate round of light parsing.
*   It can be parallelized: During execution, if a function call triggers lazy compilation, the compilation must block the main thread to preserve synchronicity. Script loading is asynchronous and therefore parsing can be more efficiently scheduled, and even happen as the script gets fetched.

However, compiling functions that are never called can waste time and memory. Like everything about performance, you must do benchmarks and weigh the different tradeoffs. The good heuristic is, as the pragma itself says: only enable this mode if the functions are _called on load_.

See also [Faster JavaScript Startup with Explicit Compile Hints](https://v8.dev/blog/explicit-compile-hints "External link (opens in new tab)")
 on v8.dev.

[Source map annotations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#source_map_annotations)

----------------------------------------------------------------------------------------------------------------------------------

Source map annotations associate JavaScript code with source files, making generated, evaluated, or minified code easier to debug.

They are specified in the TC39 specification [ECMA-426 Source map format](https://tc39.es/ecma426/ "External link (opens in new tab)")
.

### [Source URLs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#source_urls)

The following annotation gives a piece of code a URL identifier.

The syntax and placement requirements are as follows:

*   This comment be must placed at the _end_ of the script _after_ any code (other single-line comments, whitespace, and line terminators are allowed to follow it).
*   The comment must be a line comment.
*   The sigil may be a `@` instead of `#`, but `#` is preferred (`//@` might conflict with [Internet Explorer pragmas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#legacy_conditional_compilation)
    ).
*   There can be any amount of whitespace before and after `sourceURL=<url>`.
*   The `<url>` must not contain whitespace characters (they should be [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)
     as `%20`).

Source URLs are especially useful for code not originating from resources already associated with URLs, such as code executed with [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
:

The above may generate the following output in the browser console:

Hello        generated-code.js:1
Uncaught Error: error
    <anonymous> generated-code.js:1
    <anonymous> debugger eval code:1

This annotation is used by many features and is primarily associated with debugging:

*   Console/debugger output, as demonstrated above.
*   The `Error` [`stack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)
     property.
*   Resolving the `sourceMapURL`.

See also [naming evaluated code with `sourceURL`](https://developer.chrome.com/docs/devtools/javascript/source-maps#sourceurl "External link (opens in new tab)")
 on developer.chrome.com and [Give your eval a name with `//@ sourceURL`](https://web.archive.org/web/20120814122523/http://blog.getfirebug.com/2009/08/11/give-your-eval-a-name-with-sourceurl/ "External link (opens in new tab)")
 on Firebug.

### [Source map URLs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#source_map_urls)

The following annotation links generated code to a [source map](https://developer.mozilla.org/en-US/docs/Glossary/Source_map)
.

The syntax and placement requirements are the same as those of `sourceURL`.

The source map URL can be a relative URL, in which case it can be resolved to the `sourceURL`, the `<script>` element's `src` attribute, the `<script>` element's containing document's origin, etc., as defined in [ECMA 426](https://tc39.es/ecma426/#sec-linking-generated-code "External link (opens in new tab)")
. It can also be a `data:` URL containing an inline source map. The HTTP [`SourceMap`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/SourceMap)
 header takes precedence over this comment.

A debugger can use the map to display the original source and map breakpoints to a minified bundle. This is also useful in editors for go-to-definition, finding references, etc.

Build tools (bundlers, transpilers, etc.) generate this comment in the compiled output along with the map. Regular developers usually do not need to hand-write them.

[Bundler annotations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#bundler_annotations)

----------------------------------------------------------------------------------------------------------------------------

Bundlers, minifiers, and transpilers use magic comments to control code generation, optimization, and dependency handling. These annotations are consumed during the build, rather than by the JavaScript engine running the output.

There is no specification, and bundlers often invent their own annotations. This section only documents some annotations that are popular and somewhat widely supported. You must find if a bundler supports the particular annotation in its own documentation.

### [Tree shaking](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#tree_shaking)

The `/*#__PURE__*/` and `/*@__PURE__*/` annotations mark a particular function call or constructor invocation as safe to remove if the result is unused:

**Note:** This doesn't imply purity in a functional programming sense. The result might be random, depend on external state, etc. But as long as removing it doesn't change the application behavior in a way that matters, it can be annotated as pure.

Without the annotation, the bundler may need to keep the function call even if the result variable, `point`, isn't used:

With the annotation, the bundler can remove the function call entirely, and if there's no other call to `createPoint()`, the function definition as well. An incorrect annotation can cause required behavior to be removed.

The annotation applies to the particular function call. The side-effects of evaluating the argument expressions are separately decided. For example:

In this example, the `createPoint()` call is pure, and bundlers know that evaluating `1` has no side-effects. However, it cannot determine if `getY()` is pure, so the output contains the `getY()` call (and the `createPoint()` call may be retained as well). To elide everything, each function call must be separately annotated:

See also [esbuild's pure annotations](https://esbuild.github.io/api/#pure "External link (opens in new tab)")
 and [Terser's annotations](https://terser.org/docs/miscellaneous/#annotations "External link (opens in new tab)")
.

Some bundlers also recognize `/*#__NO_SIDE_EFFECTS__*/` and `/*@__NO_SIDE_EFFECTS__*/`, which annotate a function declaration, or a supported variable declaration containing a function, so calls to that function can be treated as side-effect-free:

See [Rollup's tree-shaking annotations](https://rollupjs.org/configuration-options/#treeshake-annotations "External link (opens in new tab)")
.

### [Minimization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#minimization)

There are two important minimization techniques which may be unsafe to apply: _inlining_ and _property mangling_. Inlining directly replaces a function call with the function body, while property mangling replaces property names with shorter strings.

You can use `/*@__INLINE__*/` and `/*@__NOINLINE__*/` on particular function calls to opt-in or opt-out of inlining. Things to consider:

*   Inlining may improve call performance because it avoids pushing/popping stack frames. However, the engine itself is capable of inlining and source-level inlining may change its decisions in unpredictable ways.
*   Inlining may decrease the bundle size if the function is used only once, and increase it if the function is used many times. Minimizers usually make decisions that optimize bundle size.

During property mangling, the minimizer globally replaces property names with shorter strings (while keeping distinct property names distinct). This is unsafe because the object may be accessible outside (passed to external functions, returned from exported functions, etc.), so they are usually opt-in. If you opt into mangling, you probably want to constrain mangling to name patterns known to be internal, such as names prefixed with underscores.

The `/*@__KEY__*/` annotation marks a string literal as a property name to rename. By default, the minimizer can only check for specific syntaxes, so strings passed to arbitrary functions must be explicitly marked.

The `/*@__MANGLE_PROP__*/` annotation can explicitly enable mangling for a particular property or class field.

See also [Terser Annotations](https://terser.org/docs/miscellaneous/#annotations "External link (opens in new tab)")
.

### [JSX transformation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#jsx_transformation)

JSX transpilers use file-level pragmas to select how JSX is converted into JavaScript. For example:

This generates:

These settings can also be globally configured in the transpiler; pragmas are only needed if a particular file uses a different setting.

See also [Babel's JSX transform](https://babeljs.io/docs/babel-plugin-transform-react-jsx/ "External link (opens in new tab)")
 and [esbuild's JSX configuration](https://esbuild.github.io/api/#jsx "External link (opens in new tab)")
.

[Static checker directives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#static_checker_directives)

----------------------------------------------------------------------------------------------------------------------------------------

Static checkers and related development tools also interpret comments as configuration or metadata. Some examples include:

*   **JSDoc**: [JSDoc annotations](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html "External link (opens in new tab)")
     such as `@type` and `@param` supply type information. They also power editor features such as pop-up descriptions.
*   **TypeScript (`tsc`)**: [`// @ts-check` and `// @ts-nocheck`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-3.html#errors-in-js-files-with---checkjs "External link (opens in new tab)")
     enable or disable type checking for a JavaScript file. `// @ts-ignore` suppresses diagnostics on the next line; [`// @ts-expect-error`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html#-ts-expect-error-comments "External link (opens in new tab)")
     also reports an error if there was no error to suppress.
*   **ESLint**: [Configuration comments](https://eslint.org/docs/latest/use/configure/rules "External link (opens in new tab)")
     such as `/* eslint no-console: "warn" */` configure rules, while `// eslint-disable-next-line no-console` suppresses a rule for the next line.
*   **Prettier**: [`// prettier-ignore`](https://prettier.io/docs/ignore#javascript "External link (opens in new tab)")
     excludes the next syntax node from formatting.
*   **Flow**: [`// @flow`](https://flow.org/en/docs/getting-started/ "External link (opens in new tab)")
     enables type checking for a file. [Comment types](https://flow.org/en/docs/types/comments/ "External link (opens in new tab)")
    , such as `/*: number */`, embed type syntax inside JavaScript comments.

[Legacy conditional compilation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments#legacy_conditional_compilation)

--------------------------------------------------------------------------------------------------------------------------------------------------

**Warning:** This section talks about an IE-specific mechanism. Like IE itself, it is now obsolete, but you may continue to see it in old code, and it continues to influence language design—such as why `//# sourceMapURL` is favored over `//@ sourceMapURL`. It is kept for historical interest.

Internet Explorer's JScript engine supported _conditional compilation_, an obsolete, non-standard mechanism that could interpret code inside specially marked comments. Unlike optimization hints or debugging metadata, these comments could change which code executed.

The `@cc_on` statement enabled conditional compilation. The `@set` statement defined conditional compilation variables, and `@if`, `@elif`, `@else`, and `@end` selected code based on those variables. Predefined variables included `@_jscript_version`, which identified the JScript engine version.

In a supporting engine, the assignment inside the comment would execute. Other engines would treat the entire block as an ordinary comment, leaving the variable as `false`. A line-comment form, `//@cc_on`, also existed.

See also Microsoft's historical [JScript Conditional Compilation draft](https://archives.ecma-international.org/2007/misc/jscriptconditionalcompilation2.pdf "External link (opens in new tab)")
.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Magic_comments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/magic_comments/index.md?plain=1 "Folder: en-us/web/javascript/reference/magic_comments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FMagic_comments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fmagic_comments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FMagic_comments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fmagic_comments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F90b0cce57c2c65e5c320f4cf32add4d8a50fd39c%0A*+Document+last+modified%3A+2026-10-22T17%3A43%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")