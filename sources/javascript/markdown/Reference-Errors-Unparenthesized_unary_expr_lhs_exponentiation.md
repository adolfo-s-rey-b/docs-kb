*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#mdn-search)
    

SyntaxError: unparenthesized unary expression can't appear on the left-hand side of '\*\*'
==========================================================================================

The JavaScript exception "unparenthesized unary expression can't appear on the left-hand side of '\*\*'" occurs when a unary operator (one of `typeof`, `void`, `delete`, `await`, `!`, `~`, `+`, `-`) is used on the left operand of the [exponentiation operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
 without parentheses.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#message)

------------------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Unary operator used immediately before exponentiation expression. Parenthesis must be used to disambiguate operator precedence (V8-based)
SyntaxError: unparenthesized unary expression can't appear on the left-hand side of '\*\*' (Firefox)
SyntaxError: Unexpected token '\*\*'. Ambiguous unary expression in the left hand side of the exponentiation expression; parentheses must be used to disambiguate the expression. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#error_type)

------------------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

You likely wrote something like this:

Whether it should be evaluated as `(-a) ** b` or `-(a ** b)` is ambiguous. In mathematics, -x2 means `-(x ** 2)` — and that's how many languages, including Python, Haskell, and PHP, handle it. But making the unary minus operator take precedence over `**` breaks symmetry with `a ** -b`, which is unambiguously `a ** (-b)`. Therefore, the language forbids this syntax and requires you to parenthesize either side to resolve the ambiguity.

Other unary operators cannot be the left-hand side of exponentiation either.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#examples)

--------------------------------------------------------------------------------------------------------------------------------------------

When writing complex math expressions involving exponentiation, you may write something like this:

However, the `-1 ** n` part is illegal in JavaScript. Instead, parenthesize the left operand:

This also makes the code's intent much clearer to other readers.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation#see_also)

--------------------------------------------------------------------------------------------------------------------------------------------

*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
    
*   [Original discussion of exponentiation operator precedence](https://esdiscuss.org/topic/exponentiation-operator-precedence "External link (opens in new tab)")
     on esdiscuss.org

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/unparenthesized_unary_expr_lhs_exponentiation/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/unparenthesized_unary_expr_lhs_exponentiation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnparenthesized_unary_expr_lhs_exponentiation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funparenthesized_unary_expr_lhs_exponentiation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnparenthesized_unary_expr_lhs_exponentiation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funparenthesized_unary_expr_lhs_exponentiation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")