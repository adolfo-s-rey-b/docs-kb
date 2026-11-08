*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#mdn-search)
    

return
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`return`** statement ends function execution and specifies a value to be returned to the function caller.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#try_it)

-----------------------------------------------------------------------------------------------------

    function getRectArea(width, height) {
      if (width > 0 && height > 0) {
        return width * height;
      }
      return 0;
    }
    
    console.log(getRectArea(3, 4));
    // Expected output: 12
    
    console.log(getRectArea(-3, 4));
    // Expected output: 0
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#syntax)

-----------------------------------------------------------------------------------------------------

js

    return;
    return expression;
    

[`expression` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#expression)

The expression whose value is to be returned. If omitted, `undefined` is returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#description)

---------------------------------------------------------------------------------------------------------------

The `return` statement can only be used within function bodies. When a `return` statement is used in a function body, the execution of the function is stopped. The `return` statement has different effects when placed in different functions:

*   In a plain function, the call to that function evaluates to the return value.
*   In an async function, the produced promise is resolved with the returned value.
*   In a generator function, the produced generator object's `next()` method returns `{ done: true, value: returnedValue }`.
*   In an async generator function, the produced async generator object's `next()` method returns a promise fulfilled with `{ done: true, value: returnedValue }`.

If a `return` statement is executed within a [`try`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 block, its `finally` block, if present, is first executed, before the value is actually returned.

### [Automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#automatic_semicolon_insertion)

The syntax forbids line terminators between the `return` keyword and the expression to be returned.

js

    return
    a + b;
    

The code above is transformed by [automatic semicolon insertion (ASI)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 into:

js

    return;
    a + b;
    

This makes the function return `undefined` and the `a + b` expression is never evaluated. This may generate [a warning in the console](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Stmt_after_return)
.

To avoid this problem (to prevent ASI), you could use parentheses:

js

    return (
      a + b
    );
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#examples)

---------------------------------------------------------------------------------------------------------

### [Interrupt a function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#interrupt_a_function)

A function immediately stops at the point where `return` is called.

js

    function counter() {
      // Infinite loop
      for (let count = 1; ; count++) {
        console.log(`${count}A`); // Until 5
        if (count === 5) {
          return;
        }
        console.log(`${count}B`); // Until 4
      }
      console.log(`${count}C`); // Never appears
    }
    
    counter();
    
    // Logs:
    // 1A
    // 1B
    // 2A
    // 2B
    // 3A
    // 3B
    // 4A
    // 4B
    // 5A
    

### [Returning a function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#returning_a_function)

See also the article about [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
.

js

    function magic() {
      return function calc(x) {
        return x * 42;
      };
    }
    
    const answer = magic();
    answer(1337); // 56154
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-return-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-return-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return#see_also)

---------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/return/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/return (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Freturn&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Freturn%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Freturn%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Freturn%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")