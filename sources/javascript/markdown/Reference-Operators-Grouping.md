*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#mdn-search)
    

Grouping operator ( )
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **grouping `( )`** operator controls the precedence of evaluation in expressions. It also acts as a container for arbitrary expressions in certain syntactic constructs, where ambiguity or syntax errors would otherwise occur.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#try_it)

------------------------------------------------------------------------------------------------------

    console.log(1 + 2 * 3); // 1 + 6
    // Expected output: 7
    
    console.log(1 + (2 * 3)); // 1 + 6
    // Expected output: 7
    
    console.log((1 + 2) * 3); // 3 * 3
    // Expected output: 9
    
    console.log(1 * 3 + 2 * 3); // 3 + 6
    // Expected output: 9
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#syntax)

------------------------------------------------------------------------------------------------------

js

    (expression)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#parameters)

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#expression)

Any [expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
 to be evaluated, including [comma-joined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
 expressions.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#description)

----------------------------------------------------------------------------------------------------------------

The grouping operator consists of a pair of parentheses around an expression that groups the contents. The operator overrides the normal [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
, so that operators with lower precedence (as low as the [comma](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
 operator) can be evaluated before an operator with higher precedence.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#examples)

----------------------------------------------------------------------------------------------------------

### [Using the grouping operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#using_the_grouping_operator)

Evaluating addition and subtraction before multiplication and division.

js

    const a = 1;
    const b = 2;
    const c = 3;
    
    // default precedence
    a + b * c; // 7
    // evaluated by default like this
    a + (b * c); // 7
    
    // now overriding precedence
    // addition before multiplication
    (a + b) * c; // 9
    
    // which is equivalent to
    a * c + b * c; // 9
    

Notice in these examples that the order in which the _operators_ evaluate has changed, but the order in which the _operands_ evaluate has not. For example, in this code, the function invocations `a()`, `b()`, and `c()` are evaluated left-to-right (the normal order of evaluation) before the operator order is considered.

js

    a() * (b() + c());
    

The function `a` will be called before the function `b`, which will be called before the function `c`. For more on operator precedence, see its [reference page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
.

### [Using the grouping operator to eliminate parsing ambiguity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#using_the_grouping_operator_to_eliminate_parsing_ambiguity)

An [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 cannot start with the keyword `function`, because the parser would see it as the start of a [function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
. This means the following [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 syntax is invalid:

js

    function () {
      // code
    }();
    

The grouping operator can be used to eliminate this ambiguity, since when the parser sees the left parenthesis, it knows that what follows must be an expression instead of a declaration.

js

    (function () {
      // code
    })();
    

You may also use the [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#immediately_invoked_function_expressions)
 operator to eliminate ambiguity.

In an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 expression body (one that directly returns an expression without the keyword `return`), the grouping operator can be used to return an object literal expression, because otherwise the left curly brace would be interpreted as the start of the function body.

js

    const f = () => ({ a: 1 });
    

If a property is accessed on a number literal, the [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 dot `.` may be ambiguous with a decimal point, unless the number already has a decimal point. You can wrap integer literals in parentheses to eliminate this ambiguity.

js

    (1).toString(); // "1"
    

### [Grouping operator and automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#grouping_operator_and_automatic_semicolon_insertion)

The grouping operator can mitigate [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 (ASI) pitfalls. For example, the `return` keyword and the returned expression cannot have a line break in between:

js

    function sum(a, b) {
      return
        a + b;
    }
    

This code will return `undefined`, because a semicolon is inserted directly after the `return` keyword, which causes the function to return immediately without evaluating `a + b`. In case the returned expression is long and you want to keep it well-formatted, you may use the grouping operator to signify that the `return` keyword is followed by an expression and prevent semicolon insertion:

js

    function sum(a, b) {
      return (
        a + b
      );
    }
    

However, grouping may also _introduce_ ASI hazards. When a line starts with a left parenthesis and the previous line ends with an expression, the parser will not insert a semicolon before the line break, because it could be the middle of a function call. For example:

js

    const a = 1
    (1).toString()
    

This code would be parsed as:

js

    const a = 1(1).toString();
    

Which throws "TypeError: 1 is not a function". If your coding style does not use semicolons, remember that when a line starts with a left parenthesis, _prefix_ it with a semicolon. This practice is recommended by several formatters and/or style guides, including [Prettier](https://prettier.io/docs/rationale.html#semicolons "External link (opens in new tab)")
 and [standard](https://standardjs.com/rules.html#semicolons "External link (opens in new tab)")
.

js

    const a = 1
    ;(1).toString()
    

For more advice on working with ASI, see its [reference section](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-grouping-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-grouping-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping#see_also)

----------------------------------------------------------------------------------------------------------

*   [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
    
*   [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
    
*   [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/grouping/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/grouping (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FGrouping&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fgrouping%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FGrouping%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fgrouping%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")