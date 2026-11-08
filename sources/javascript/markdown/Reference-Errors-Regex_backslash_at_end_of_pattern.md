*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#mdn-search)
    

SyntaxError: \\ at end of pattern
=================================

The JavaScript exception "\\ at end of pattern" occurs when a regular expression pattern ends with an unescaped backslash (`\`). In a regex literal, the backslash would cause the closing slash `/` to be a literal character, so this can only appear when using the [`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
 constructor.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#message)

------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid regular expression: /\\/: \\ at end of pattern (V8-based)
SyntaxError: \\ at end of pattern (Firefox)
SyntaxError: Invalid regular expression: \\ at end of pattern (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#error_type)

------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------------------------

A backslash cannot appear literally in a regular expression. It either precedes another character to [escape it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#escape_sequences)
, or is itself escaped by another backslash. A backslash at the end of a regular expression pattern is invalid because it is not escaping anything.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#examples)

--------------------------------------------------------------------------------------------------------------------------------

### [Double-escaping backslashes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#double-escaping_backslashes)

This error can only happen when using the `RegExp()` constructor. Consider the following code, which intends to match a single backslash character:

In JavaScript strings, backslashes are also escape sequences. Therefore, the two backslashes in the string literal `"\\"` are interpreted as a single backslash. The `RegExp()` constructor then only sees a single backslash character in the regex source. To fix this, you need to double-escape the backslash:

The four backslashes in the string literal represent two backslashes in the regex source, which then becomes a [character escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
 for a single backslash literal character.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern#see_also)

--------------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#escape_sequences)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_backslash_at_end_of_pattern/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/regex_backslash_at_end_of_pattern/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/regex_backslash_at_end_of_pattern (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_backslash_at_end_of_pattern&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_backslash_at_end_of_pattern%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_backslash_at_end_of_pattern%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_backslash_at_end_of_pattern%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")