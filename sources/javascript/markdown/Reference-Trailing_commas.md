*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#mdn-search)
    

Trailing commas
===============

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Trailing commas** (sometimes called "final commas") can be useful when adding new elements, parameters, or properties to JavaScript code. If you want to add a new property, you can add a new line without modifying the previously last line if that line already uses a trailing comma. This makes version-control diffs cleaner and editing code might be less troublesome.

JavaScript has allowed trailing commas in array literals since the beginning. Trailing commas are now also allowed in object literals, function parameters, named imports, named exports, and more.

[JSON](https://developer.mozilla.org/en-US/docs/Glossary/JSON)
, however, disallows all trailing commas.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#description)

-------------------------------------------------------------------------------------------------------------

JavaScript allows trailing commas wherever a comma-separated list of values is accepted and more values may be expected after the last item. This includes:

*   [Array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#arrays)
    
*   [Object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#objects)
    
*   [Parameter definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#parameter_definitions)
    
*   [Function calls](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#function_calls)
    
*   [Named imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#named_imports)
    
*   [Named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#named_exports)
    
*   [Dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_dynamic_import)
    
*   [Array and object destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_destructuring)
    

In all these cases, the trailing comma is entirely optional and doesn't change the program's semantics in any way.

It is particularly useful when adding, removing, or reordering items in a list that spans multiple lines, because it reduces the number of lines that need to be changed, which helps with both editing and reviewing the diff.

diff

      [\
        "foo",\
    +   "baz",\
        "bar",\
    -   "baz",\
      ]
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#examples)

-------------------------------------------------------------------------------------------------------

### [Trailing commas in literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_literals)

#### Arrays

JavaScript ignores trailing commas in array literals:

js

    const arr = [\
      1,\
      2,\
      3,\
    ];
    
    arr; // [1, 2, 3]
    arr.length; // 3
    

If more than one trailing comma is used, an elision (or hole) is produced. An array with holes is called [_sparse_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
 (a _dense_ array has no holes). When iterating arrays for example with [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 or [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, array holes are skipped. Sparse arrays are generally unfavorable, so you should avoid having multiple trailing commas.

js

    const arr = [1, 2, 3, , ,];
    arr.length; // 5
    

#### Objects

Trailing commas in object literals are legal as well:

js

    const object = {
      foo: "bar",
      baz: "qwerty",
      age: 42,
    };
    

### [Trailing commas in functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_functions)

Trailing commas are also allowed in function parameter lists.

#### Parameter definitions

The following function definition pairs are legal and equivalent to each other. Trailing commas don't affect the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
 property of function declarations or their [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object.

js

    function f(p) {}
    function f(p,) {}
    
    (p) => {};
    (p,) => {};
    

The trailing comma also works with [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
 for classes or objects:

js

    class C {
      one(a,) {}
      two(a, b,) {}
    }
    
    const obj = {
      one(a,) {},
      two(a, b,) {},
    };
    

#### Function calls

The following function invocation pairs are legal and equivalent to each other.

js

    f(p);
    f(p,);
    
    Math.max(10, 20);
    Math.max(10, 20,);
    

#### Illegal trailing commas

Function parameter definitions or function invocations only containing a comma will throw a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
. Furthermore, when using [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
, trailing commas are not allowed:

js

    function f(,) {} // SyntaxError: missing formal parameter
    (,) => {};       // SyntaxError: expected expression, got ','
    f(,)             // SyntaxError: expected expression, got ','
    
    function f(...p,) {} // SyntaxError: parameter after rest parameter
    (...p,) => {}        // SyntaxError: expected closing parenthesis, got ','
    

### [Trailing commas in destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_destructuring)

A trailing comma is also allowed within a [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 pattern:

js

    // array destructuring with trailing comma
    [a, b,] = [1, 2];
    
    // object destructuring with trailing comma
    const o = {
      p: 42,
      q: true,
    };
    const { p, q, } = o;
    

However, a trailing comma is not allowed after the rest element, if present

js

    const [a, ...b,] = [1, 2, 3];
    // SyntaxError: rest element may not have a trailing comma
    

### [Trailing commas in JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_json)

As JSON is based on a very restricted subset of JavaScript syntax, **trailing commas are not allowed in JSON**.

Both lines will throw a `SyntaxError`:

js

    JSON.parse("[1, 2, 3, 4, ]");
    JSON.parse('{"foo" : 1, }');
    // SyntaxError JSON.parse: unexpected character
    // at line 1 column 14 of the JSON data
    

Omit the trailing commas to parse the JSON correctly:

js

    JSON.parse("[1, 2, 3, 4 ]");
    JSON.parse('{"foo" : 1 }');
    

### [Trailing commas in named imports and named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_named_imports_and_named_exports)

Trailing commas are valid in [named imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#named_import)
 and [named exports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
.

#### Named imports

js

    import {
      A,
      B,
      C,
    } from "D";
    
    import { X, Y, Z, } from "W";
    
    import { A as B, C as D, E as F, } from "Z";
    

#### Named exports

js

    export {
      A,
      B,
      C,
    };
    
    export { A, B, C, };
    
    export { A as B, C as D, E as F, };
    

### [Trailing commas in dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#trailing_commas_in_dynamic_import)

Trailing commas are only allowed in [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 if the runtime also implements the second `options` parameter.

js

    import("D",);
    import(
      "D",
      { with: { type: "json" } },
    );
    

### [Quantifier prefix](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#quantifier_prefix)

**Note:** The trailing comma in a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)
 actually changes its semantics from matching "exactly `n`" to matching "at least `n`".

js

    /x{2}/; // Exactly 2 occurrences of "x"; equivalent to /xx/
    /x{2,}/; // At least 2 occurrences of "x"; equivalent to /xx+/
    /x{2,4}/; // 2 to 4 occurrences of "x"; equivalent to /xxx?x?/
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-Elision](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-Elision) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ObjectLiteral](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ObjectLiteral) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ArrayLiteral](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ArrayLiteral) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-Arguments](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-Arguments) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-FormalParameters](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-FormalParameters) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-CoverParenthesizedExpressionAndArrowParameterList](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-CoverParenthesizedExpressionAndArrowParameterList) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-NamedImports](https://tc39.es/ecma262/multipage/ecmascript-language-scripts-and-modules.html#prod-NamedImports) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-NamedExports](https://tc39.es/ecma262/multipage/ecmascript-language-scripts-and-modules.html#prod-NamedExports) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-QuantifierPrefix](https://tc39.es/ecma262/multipage/text-processing.html#prod-QuantifierPrefix) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-annexB-InvalidBracedQuantifier](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#prod-annexB-InvalidBracedQuantifier) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#see_also)

-------------------------------------------------------------------------------------------------------

*   [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/trailing_commas/index.md?plain=1 "Folder: en-us/web/javascript/reference/trailing_commas (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FTrailing_commas&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ftrailing_commas%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FTrailing_commas%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ftrailing_commas%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")