*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#mdn-search)
    

SyntaxError: incomplete quantifier in regular expression
========================================================

The JavaScript exception "incomplete quantifier in regular expression" occurs when a regular expression pattern contains a `{`, but it does not start a valid [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#message)

------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid regular expression: /1{/u: Incomplete quantifier (V8-based)
SyntaxError: incomplete quantifier in regular expression (Firefox)
SyntaxError: Invalid regular expression: incomplete {} quantifier for Unicode pattern (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#error_type)

------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------------------

A `{` character in a regular expression pattern starts a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
. A valid quantifier is in the form `{n}`, `{n,}`, or `{n,m}`, where `n` and `m` are non-negative integers and `m` is not less than `n`. If the `{` character does not start a valid quantifier, a `SyntaxError` occurs.

In Unicode-unaware mode, this syntax causes the `{` to become a literal character instead of generating an error, but this is a [deprecated syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
 and you should not rely on it.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#examples)

--------------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#invalid_cases)

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Quantifier: `*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_incomplete_quantifier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/regex_incomplete_quantifier/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/regex_incomplete_quantifier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_incomplete_quantifier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_incomplete_quantifier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_incomplete_quantifier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_incomplete_quantifier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")