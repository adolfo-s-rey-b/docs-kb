*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#mdn-search)
    

SyntaxError: string literal contains an unescaped line break
============================================================

The JavaScript error "string literal contains an unescaped line break" occurs when there is an unterminated [string literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#string_literals)
 somewhere. String literals must be enclosed by single (`'`) or double (`"`) quotes and cannot split across multiple lines.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#message)

---------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid or unexpected token (V8-based)
SyntaxError: '' string literal contains an unescaped line break (Firefox)
SyntaxError: Unexpected EOF (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#error_type)

---------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

There is an unterminated [string literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#string_literals)
 somewhere. String literals must be enclosed by single (`'`) or double (`"`) quotes. JavaScript makes no distinction between single-quoted strings and double-quoted strings. [Escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#escape_sequences)
 work in strings created with either single or double quotes. To fix this error, check if:

*   you have opening and closing quotes (single or double) for your string literal,
*   you have escaped your string literal correctly,
*   your string literal isn't split across multiple lines.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#examples)

-----------------------------------------------------------------------------------------------------------------

### [Multiple lines](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#multiple_lines)

You can't split a string across multiple lines like this in JavaScript:

Instead, use the [\+ operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
, a backslash, or [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
. The `+` operator variant looks like this:

Or you can use the backslash character ("\\") at the end of each line to indicate that the string will continue on the next line. Make sure there is no space or any other character after the backslash (except for a line break), or as an indent; otherwise it will not work. That form looks like this:

Another possibility is to use [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [string literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#string_literals)
    
*   [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/String_literal_EOL/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/string_literal_eol/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/string_literal_eol (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FString_literal_EOL&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fstring_literal_eol%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FString_literal_EOL%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fstring_literal_eol%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")