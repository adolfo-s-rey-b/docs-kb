*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#mdn-search)
    

SyntaxError: cannot use ?? unparenthesized within || and && expressions
=======================================================================

The JavaScript exception "cannot use `??` unparenthesized within `||` and `&&` expressions" occurs when a [nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
 is used with a [logical OR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR)
 or [logical AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)
 in the same expression without parentheses.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#message)

----------------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Unexpected token '??' (V8-based)
SyntaxError: cannot use \`??\` unparenthesized within \`||\` and \`&&\` expressions (Firefox)
SyntaxError: Unexpected token '??'. Coalescing and logical operators used together in the same expression; parentheses must be used to disambiguate. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#error_type)

----------------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------------------------------

The [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 chain looks like this:

|   >   &&   >   ||   >   =
|   >   ??   >   =

However, the precedence _between_ `??` and `&&`/`||` is intentionally undefined, because the short circuiting behavior of logical operators can make the expression's evaluation counter-intuitive. Therefore, the following combinations are all syntax errors, because the language doesn't know how to parenthesize the operands:

Instead, make your intent clear by parenthesizing either side explicitly:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#examples)

------------------------------------------------------------------------------------------------------------------------------------------

When migrating legacy code that uses `||` and `&&` for guarding against `null` or `undefined`, you may often convert it partially:

Instead, consider parenthesizing the `&&`:

Even better, consider using [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
 instead of `&&`:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized#see_also)

------------------------------------------------------------------------------------------------------------------------------------------

*   [Issue about nullish coalescing precedence](https://github.com/tc39/proposal-nullish-coalescing/issues/15 "External link (opens in new tab)")
     in the TC39 nullish-coalescing proposal
*   [Nullish coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
    
*   [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_use_nullish_coalescing_unparenthesized/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_use_nullish_coalescing_unparenthesized/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_use_nullish_coalescing_unparenthesized (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_use_nullish_coalescing_unparenthesized&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_use_nullish_coalescing_unparenthesized%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_use_nullish_coalescing_unparenthesized%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_use_nullish_coalescing_unparenthesized%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848dba3f268442d9c91a08c5c825af77c583789b%0A*+Document+last+modified%3A+2026-03-20T15%3A48%3A18.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")