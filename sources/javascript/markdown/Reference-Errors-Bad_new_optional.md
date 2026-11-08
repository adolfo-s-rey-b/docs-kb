*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#mdn-search)
    

SyntaxError: new keyword cannot be used with an optional chain
==============================================================

The JavaScript exception "new keyword cannot be used with an optional chain" occurs when the constructor of a [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 expression is an [optional chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
, or if there's an optional chain between the constructor and the parenthesized list of arguments.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#message)

-------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid optional chain from new expression (V8-based)
SyntaxError: new keyword cannot be used with an optional chain (Firefox)
SyntaxError: Cannot call constructor in an optional chain. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#error_type)

-------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------

There are two ways to get this error. The first one is if the constructor expression is an optional chain expression, like this:

The second one is if `?.` occurs between the constructor and the arguments list, like this:

Optional `new` is specifically forbidden because its syntax is complicated (`new` with and without arguments), and the result is unclear (it would be the only case where `new` does not evaluate to an object value). You need to translate the optional chaining to its underlying condition (see [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
 for more information).

Remember that optional chaining only short-circuits within a parenthesized unit. If you parenthesize your constructor expression, the optional chaining will not cause an error, because now the constructor does not short-circuit and the result is clear (the constructor will produce `undefined` and then cause the `new` expression to throw).

However this is a bit nonsensical anyway because optional chaining prevents errors inside the property access chain, but is then guaranteed to generate an error when calling `new`. You would probably still want to use a conditional check.

Note that optional chaining is only forbidden as the constructor expression. You can use optional chaining inside the argument list, or use optional chaining on the `new` expression as a whole.

Note that there's no needs to use `?.` on the `new` expression itself: `new a()?.b`, because `new` is guaranteed to produce a non-nullish object value.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    
*   [Optional chaining (`?.`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
    
*   [Original discussion on whether "optional new" should be allowed](https://github.com/tc39/proposal-optional-chaining/issues/22 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_new_optional/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bad_new_optional/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bad_new_optional (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_new_optional&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_new_optional%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_new_optional%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_new_optional%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")