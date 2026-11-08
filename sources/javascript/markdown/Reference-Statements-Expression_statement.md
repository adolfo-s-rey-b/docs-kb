*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#mdn-search)
    

Expression statement
====================

An **expression statement** is an expression used in a place where a statement is expected. The expression is evaluated and its result is discarded — therefore, it makes sense only for expressions that have side effects, such as executing a function or updating a variable.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#syntax)

-------------------------------------------------------------------------------------------------------------------

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#expression)

An arbitrary [expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
 to be evaluated. There are [certain expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#forbidden_expressions)
 that may be ambiguous with other statements and are thus forbidden.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#description)

-----------------------------------------------------------------------------------------------------------------------------

Apart from the [dedicated statement syntaxes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
, you can also use almost any [expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
 as a statement on its own. The expression statement syntax requires a semicolon at the end, but the [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 process may insert one for you if the lack of a semicolon results in invalid syntax.

Because the expression is evaluated and then discarded, the result of the expression is not available. Therefore, the expression must have some side effect for it to be useful. Expression statements are commonly:

*   Function calls (`console.log("Hello");`, `[1, 2, 3].forEach((i) => console.log(i));`)
*   [Tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
    
*   [Assignment expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#assignment_operators)
    , including compound assignments
*   [Increment and decrement operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement)
    
*   [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
    
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    
*   [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
     and [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
    

Others may also have side effects if they invoke [getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 or trigger [type coercions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#type_coercion)
.

### [Forbidden expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#forbidden_expressions)

In order for an expression to be used as a statement, it must not be ambiguous with other statement syntaxes. Therefore, the expression must not start with any of the following tokens:

*   `function`: which would be a [`function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
     or [`function*` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    , not a [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
     or [`function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
    
*   `async function`: which would be an [`async function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
     or [`async function*` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
    , not an [`async function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function)
     or [`async function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function*)
    
*   `class`: which would be a [`class` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    , not a [`class` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
    
*   `let[`: which would be a [`let` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)\
     with [array destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)\
    , not a [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)\
     on a variable called `let` (`let` can only be an identifier in [non-strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#extra_reserved_words)\
    )\
*   `{`: which would be a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)\
    , not an [object literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)\
    \
\
Therefore, all of the following are invalid:\
\
More dangerously, sometimes the code happens to be valid syntax, but is not what you intend.\
\
To avoid these problems, you can use parentheses, so that the statement is unambiguously an expression statement.\
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#examples)\
\
-----------------------------------------------------------------------------------------------------------------------\
\
### [Avoiding control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#avoiding_control_flow_statements)\
\
You can avoid almost all use of control flow statements using expression statements. For example, `if...else` can be replaced with [ternary operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)\
 and [logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators)\
. Iterative statements like `for` or `for...of` can be replaced with [array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)\
.\
\
**Warning:** This only demonstrates a capability of the language. Excessive use of expression statements as a substitute for control-flow statements can make code much less readable.\
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#specifications)\
\
-----------------------------------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [ECMAScript® 2027 Language Specification  <br>\# sec-expression-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-expression-statement) |\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement#see_also)\
\
-----------------------------------------------------------------------------------------------------------------------\
\
*   [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)\
    \
*   [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)\
    \
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/expression_statement/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/expression_statement (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2FExpression_statement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fexpression_statement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2FExpression_statement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fexpression_statement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")