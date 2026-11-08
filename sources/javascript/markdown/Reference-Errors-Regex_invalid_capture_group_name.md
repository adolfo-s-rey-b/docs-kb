*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#mdn-search)
    

SyntaxError: invalid capture group name in regular expression
=============================================================

The JavaScript exception "invalid capture group name in regular expression" occurs when a [named capturing group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
 or [named backreference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_backreference)
 contains an invalid [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#message)

-----------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid regular expression: /(?<1>)/: Invalid capture group name (V8-based)
SyntaxError: invalid capture group name in regular expression (Firefox)
SyntaxError: Invalid regular expression: invalid group specifier name (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#error_type)

-----------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------------------------

Each named capturing group must have a name that is a valid identifier. You cannot use arbitrary strings as the group identifier.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#examples)

-------------------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#invalid_cases)

Or you might be building the regex dynamically:

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#valid_cases)

If the regex is built dynamically, make sure the names are all valid identifiers. For example:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Named capturing group: `(?<name>...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_invalid_capture_group_name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/regex_invalid_capture_group_name/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/regex_invalid_capture_group_name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_invalid_capture_group_name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_invalid_capture_group_name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_invalid_capture_group_name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_invalid_capture_group_name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")