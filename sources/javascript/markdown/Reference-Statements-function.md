*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#mdn-search)
    

function
========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`function`** declaration creates a [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 of a new function to a given name.

You can also define functions using the [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#try_it)

-------------------------------------------------------------------------------------------------------

    function calcRectArea(width, height) {
      return width * height;
    }
    
    console.log(calcRectArea(5, 6));
    // Expected output: 30
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#syntax)

-------------------------------------------------------------------------------------------------------

js

    function name(param0) {
      statements
    }
    function name(param0, param1) {
      statements
    }
    function name(param0, param1, /* …, */ paramN) {
      statements
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#parameters)

[`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#name)

The function name.

[`param` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#param)

The name of a formal parameter for the function. Maximum number of arguments varies in different engines. For the parameters' syntax, see the [Functions reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_parameters)
.

[`statements` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#statements)

The statements which comprise the body of the function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#description)

-----------------------------------------------------------------------------------------------------------------

A `function` declaration creates a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 object. Each time when a function is called, it returns the value specified by the last executed [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement, or `undefined` if the end of the function body is reached. See [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 for detailed information on functions.

`function` declarations behave like a mix of [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
 and [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
:

*   Like `let`, in strict mode, [function declarations are scoped to the most closely containing block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#block-level_function_declaration)
    .
*   Like `let`, function declarations at the top level of a module or within blocks in strict mode cannot be [redeclared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#redeclarations)
     by any other declaration.
*   Like `var`, function declarations at the top level of a script (strict or non-strict) become properties on [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
    . Function declarations at the top level of a script or function body (strict or non-strict) can be redeclared by another `function` or `var`.
*   Like both, function declarations can be re-assigned, but you should avoid doing so.
*   Unlike either, function declarations are [hoisted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#hoisting)
     together with its value and can be called anywhere in its scope.

### [Block-level function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#block-level_function_declaration)

**Warning:** In [non-strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, function declarations inside blocks behave strangely. Only declare functions in blocks if you are in strict mode.

Functions can be conditionally declared — that is, a function statement can be nested within an [`if`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 statement. However, in non-strict mode, the results are inconsistent across implementations.

js

    console.log(
      `'foo' name ${
        "foo" in globalThis ? "is" : "is not"
      } global. typeof foo is ${typeof foo}`,
    );
    if (false) {
      function foo() {
        return 1;
      }
    }
    
    // In Chrome:
    // 'foo' name is global. typeof foo is undefined
    //
    // In Firefox:
    // 'foo' name is global. typeof foo is undefined
    //
    // In Safari:
    // 'foo' name is global. typeof foo is function
    

The scoping and hoisting effect won't change regardless of whether the `if` body is actually executed.

js

    console.log(
      `'foo' name ${
        "foo" in globalThis ? "is" : "is not"
      } global. typeof foo is ${typeof foo}`,
    );
    if (true) {
      function foo() {
        return 1;
      }
    }
    
    // In Chrome:
    // 'foo' name is global. typeof foo is undefined
    //
    // In Firefox:
    // 'foo' name is global. typeof foo is undefined
    //
    // In Safari:
    // 'foo' name is global. typeof foo is function
    

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
\-level function declarations are scoped to that block and are hoisted to the top of the block.

js

    "use strict";
    
    {
      foo(); // Logs "foo"
      function foo() {
        console.log("foo");
      }
    }
    
    console.log(
      `'foo' name ${
        "foo" in globalThis ? "is" : "is not"
      } global. typeof foo is ${typeof foo}`,
    );
    // 'foo' name is not global. typeof foo is undefined
    

### [Hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#hoisting)

Function declarations in JavaScript are [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
 to the top of the enclosing function or global scope. You can use the function before you declared it:

js

    hoisted(); // Logs "foo"
    
    function hoisted() {
      console.log("foo");
    }
    

Note that [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 are not hoisted:

js

    notHoisted(); // TypeError: notHoisted is not a function
    
    var notHoisted = function () {
      console.log("bar");
    };
    

### [Redeclarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#redeclarations)

Whether `function` declarations can be redeclared in the same scope depends on what scope it's contained in.

At the top level of a script, `function` declarations behave like `var` and can be redeclared by another `function` or `var` but not by [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, or [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
.

js

    function a(b) {}
    function a(b, c) {}
    console.log(a.length); // 2
    let a = 2; // SyntaxError: Identifier 'a' has already been declared
    

When `function` declarations are redeclared by `var`, the `var` declaration's initializer always overrides the function's value, regardless of their relative position. This is because function declarations are hoisted before any initializer gets evaluated, so the initializer comes later and overrides the value.

js

    var a = 1;
    function a() {}
    console.log(a); // 1
    

At the top level of a function's body, `function` also behaves like `var` and can be redeclared or have the same name as a parameter.

js

    function foo(a) {
      function a() {}
      console.log(typeof a);
    }
    
    foo(2); // Logs "function"
    

At the top level of a module or a block in strict mode, `function` declarations behave like `let` and cannot be redeclared by any other declaration.

js

    // Assuming current source is a module
    function foo() {}
    function foo() {} // SyntaxError: Identifier 'foo' has already been declared
    

js

    "use strict";
    {
      function foo() {}
      function foo() {} // SyntaxError: Identifier 'foo' has already been declared
    }
    

A `function` declaration within a `catch` block cannot have the same name as the `catch`\-bound identifier, even in non-strict mode.

js

    try {
    } catch (e) {
      function e() {} // SyntaxError: Identifier 'e' has already been declared
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#examples)

-----------------------------------------------------------------------------------------------------------

### [Using function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#using_function)

The following code declares a function that returns the total amount of sales, when given the number of units sold of three products.

js

    function calcSales(unitsA, unitsB, unitsC) {
      return unitsA * 79 + unitsB * 129 + unitsC * 699;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    
*   [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
    
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/function/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffunction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffunction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffunction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffunction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")