*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#mdn-search)
    

Logical NOT (!)
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **logical NOT (`!`)** (logical complement, negation) operator takes truth to falsity and vice versa. It is typically used with boolean (logical) values. When used with non-Boolean values, it returns `false` if its single operand can be converted to `true`; otherwise, returns `true`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#try_it)

---------------------------------------------------------------------------------------------------------

    const a = 3;
    const b = -2;
    
    console.log(!(a > 0 || b > 0));
    // Expected output: false
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#syntax)

---------------------------------------------------------------------------------------------------------

js

    !x
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#description)

-------------------------------------------------------------------------------------------------------------------

Returns `false` if its single operand can be converted to `true`; otherwise, returns `true`.

If a value can be converted to `true`, the value is so-called [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
. If a value can be converted to `false`, the value is so-called [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
.

Examples of expressions that can be converted to false are:

*   `null`;
*   `NaN`;
*   `0`;
*   empty string (`""` or `''` or ` `` `);
*   `undefined`.

Even though the `!` operator can be used with operands that are not Boolean values, it can still be considered a boolean operator since its return value can always be converted to a [boolean primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
. To explicitly convert its return value (or any expression in general) to the corresponding boolean value, use a double NOT operator (`!!`) or the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
 constructor.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#examples)

-------------------------------------------------------------------------------------------------------------

### [Using NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#using_not)

The following code shows examples of the `!` (logical NOT) operator.

js

    !true; // !t returns false
    !false; // !f returns true
    !""; // !f returns true
    !"Cat"; // !t returns false
    

### [Double NOT (`!!`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#double_not_!!)

It is possible to use a couple of NOT operators in series to explicitly force the conversion of any value to the corresponding [boolean primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
. The conversion is based on the "truthiness" or "falsiness" of the value (see [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 and [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
).

The same conversion can be done through the [`Boolean()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
 function.

js

    !!true; // !!truthy returns true
    !!{}; // !!truthy returns true: any object is truthy…
    !!new Boolean(false); // … even Boolean objects with a false .valueOf()!
    !!false; // !!falsy returns false
    !!""; // !!falsy returns false
    !!Boolean(false); // !!falsy returns false
    

### [Converting between NOTs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#converting_between_nots)

The following operation involving **booleans**:

js

    !!bCondition
    

is always equal to:

js

    bCondition
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-logical-not-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-logical-not-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
    
*   [Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    
*   [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/logical_not/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/logical_not (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_NOT&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_not%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_NOT%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_not%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")