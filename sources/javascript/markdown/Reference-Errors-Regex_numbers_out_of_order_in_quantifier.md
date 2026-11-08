*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#mdn-search)
    

SyntaxError: numbers out of order in {} quantifier.
===================================================

The JavaScript exception "numbers out of order in {} quantifier" occurs when a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
 in a regular expression uses the `{n,m}` syntax but `m` is less than `n`.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#message)

-------------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid regular expression: /1{2,1}/: numbers out of order in {} quantifier (V8-based)
SyntaxError: numbers out of order in {} quantifier. (Firefox)
SyntaxError: Invalid regular expression: numbers out of order in {} quantifier (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#error_type)

-------------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------------------------

The `{n,m}` syntax in a regular expression is used to specify that the preceding item is to be matched at least `n` times, but not more than `m` times. If `m` is less than `n`, the quantifier is nonsensical because, for example, a character cannot appear at least 2 times but not more than 1 time. Therefore, an error is thrown.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#examples)

---------------------------------------------------------------------------------------------------------------------------------------

### [Invalid examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#invalid_examples)

### [Valid examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#valid_examples)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier#see_also)

---------------------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Quantifier: `*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_numbers_out_of_order_in_quantifier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/regex_numbers_out_of_order_in_quantifier/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/regex_numbers_out_of_order_in_quantifier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_numbers_out_of_order_in_quantifier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_numbers_out_of_order_in_quantifier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_numbers_out_of_order_in_quantifier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_numbers_out_of_order_in_quantifier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")