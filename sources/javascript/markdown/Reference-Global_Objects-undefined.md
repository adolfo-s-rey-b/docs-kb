*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#mdn-search)
    

undefined
=========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`undefined`** global property represents the primitive value [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#undefined_type)
. It is one of JavaScript's [primitive types](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#try_it)

------------------------------------------------------------------------------------------------------------

    function test(t) {
      if (t === undefined) {
        return "Undefined value!";
      }
      return t;
    }
    
    let x;
    
    console.log(test(x));
    // Expected output: "Undefined value!"
    

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#value)

----------------------------------------------------------------------------------------------------------

The primitive value [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#undefined_type)
.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#description)

----------------------------------------------------------------------------------------------------------------------

`undefined` is a property of the _global object_. That is, it is a variable in global scope.

In all non-legacy browsers, `undefined` is a non-configurable, non-writable property. Even when this is not the case, avoid overriding it.

A variable that has not been assigned a value is of type `undefined`. A function returns `undefined` if a value was not [`returned`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
. Accessing a property that does not exist also returns `undefined`. The [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
 operator always returns `undefined`.

**Note:** While you can use `undefined` as an [identifier](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
 (variable name) in any scope other than the global scope (because `undefined` is not a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
), doing so is a very bad idea that will make your code difficult to maintain and debug.

js

    // DON'T DO THIS
    
    (() => {
      const undefined = "foo";
      console.log(undefined, typeof undefined); // foo string
    })();
    
    ((undefined) => {
      console.log(undefined, typeof undefined); // foo string
    })("foo");
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#examples)

----------------------------------------------------------------------------------------------------------------

### [Strict equality and undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#strict_equality_and_undefined)

You can use `undefined` and the strict equality and inequality operators to determine whether a variable has a value. In the following code, the variable `x` is not initialized, and the `if` statement evaluates to true.

js

    let x;
    if (x === undefined) {
      // these statements execute
    } else {
      // these statements do not execute
    }
    

**Note:** The _strict equality_ operator (as opposed to the _loose equality_ operator) must be used here, because `x == undefined` also checks whether `x` is `null`, while strict equality doesn't. This is because `null` is not equivalent to `undefined`.

See [Equality comparison and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
 for details.

### [typeof operator and undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#typeof_operator_and_undefined)

[`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 can also determine whether a variable is `undefined`:

js

    let x;
    if (typeof x === "undefined") {
      // these statements execute
    }
    

One reason to use [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 is that it does not throw an error if the variable does not exist in the current scope.

js

    // x has not been declared before
    // evaluates to true without errors
    if (typeof x === "undefined") {
      // these statements execute
    }
    
    // Throws a ReferenceError
    if (x === undefined) {
    }
    

It also works with variables declared with `var` _after_ the check, because the declaration is hoisted to the top of the scope with value `undefined`.

js

    if (typeof x === "undefined") {
      // these statements execute
    }
    var x = 1;
    

This technique is usually only useful for testing global variables. You can know if a variable exists at any other scope (blocks, functions, modules, etc.) just by looking at the source code. The global scope is bound to the [global object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
, so checking the existence of a variable in the global context can be done by checking the existence of a property on the _global object_, such as by using the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator:

js

    if ("x" in window) {
      // These statements execute only if x is defined globally
    }
    

However, none of the techniques above work if the variable is declared with `let`, `const`, or other lexical declarations. Using `typeof` before the line of declaration still produces a `ReferenceError`, due to the [temporal dead zone (TDZ)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
.

js

    if (typeof z === "undefined") {
      // Uncaught ReferenceError: Cannot access 'z' before initialization
    }
    let z = 1;
    

Furthermore, `let` and `const` declarations do not create properties on the global object, so they cannot be checked with the `in` operator either.

js

    let z;
    if ("z" in window) {
      // false, even if z is declared globally with let or const
    }
    

If you want to share global variables across different scripts, it is more advisable to use `var` or explicitly attach them to the global object:

js

    window.myGlobalVar = "foo";
    

### [void operator and undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#void_operator_and_undefined)

The [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
 operator can also be used to produce the `undefined` value. This is very commonly seen in minified code because `void 0` is 3 bytes shorter and cannot be overridden. You should usually avoid this pattern in your own code.

js

    let x;
    if (x === void 0) {
      // these statements execute
    }
    
    // y has not been declared before
    if (y === void 0) {
      // throws Uncaught ReferenceError: y is not defined
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-undefined](https://tc39.es/ecma262/multipage/global-object.html#sec-undefined) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#see_also)

----------------------------------------------------------------------------------------------------------------

*   [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
    
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/undefined/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/undefined (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2Fundefined&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fundefined%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2Fundefined%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fundefined%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5ebca2edd6095fb3f61d442ed3146fa37fffbf7d%0A*+Document+last+modified%3A+2026-01-10T02%3A43%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")