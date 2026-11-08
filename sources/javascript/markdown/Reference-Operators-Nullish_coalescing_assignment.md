*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#mdn-search)
    

Nullish coalescing assignment (??=)
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **nullish coalescing assignment (`??=`)** operator, also known as the **logical nullish assignment** operator, only evaluates the right operand and assigns to the left if the left operand is [nullish](https://developer.mozilla.org/en-US/docs/Glossary/Nullish)
 (`null` or `undefined`).

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#try_it)

---------------------------------------------------------------------------------------------------------------------------

    const a = { duration: 50 };
    
    a.speed ??= 25;
    console.log(a.speed);
    // Expected output: 25
    
    a.duration ??= 10;
    console.log(a.duration);
    // Expected output: 50
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#syntax)

---------------------------------------------------------------------------------------------------------------------------

js

    x ??= y
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#description)

-------------------------------------------------------------------------------------------------------------------------------------

Nullish coalescing assignment [_short-circuits_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#short-circuiting)
, meaning that `x ??= y` is equivalent to `x ?? (x = y)`, except that the expression `x` is only evaluated once.

No assignment is performed if the left-hand side is not nullish, due to short-circuiting of the [nullish coalescing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
 operator. For example, the following does not throw an error, despite `x` being `const`:

js

    const x = 1;
    x ??= 2;
    

Neither would the following trigger the setter:

js

    const x = {
      get value() {
        return 1;
      },
      set value(v) {
        console.log("Setter called");
      },
    };
    
    x.value ??= 2;
    

In fact, if `x` is not nullish, `y` is not evaluated at all.

js

    const x = 1;
    x ??= console.log("y evaluated");
    // Logs nothing
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#examples)

-------------------------------------------------------------------------------------------------------------------------------

### [Using nullish coalescing assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#using_nullish_coalescing_assignment)

You can use the nullish coalescing assignment operator to apply default values to object properties. Compared to using destructuring and [default values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#default_value)
, `??=` also applies the default value if the property has value `null`.

js

    function config(options) {
      options.duration ??= 100;
      options.speed ??= 25;
      return options;
    }
    
    config({ duration: 125 }); // { duration: 125, speed: 25 }
    config({}); // { duration: 100, speed: 25 }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-assignment-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-assignment-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [Nullish coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
    
*   [Nullish](https://developer.mozilla.org/en-US/docs/Glossary/Nullish)
    
*   [Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    
*   [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/nullish_coalescing_assignment/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/nullish_coalescing_assignment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FNullish_coalescing_assignment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnullish_coalescing_assignment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FNullish_coalescing_assignment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnullish_coalescing_assignment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")