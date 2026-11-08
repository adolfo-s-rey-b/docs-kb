*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#mdn-search)
    

SyntaxError: illegal character
==============================

The JavaScript exception "illegal character" occurs when the [lexer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
 reads a character that's not part of a string literal, and the character cannot constitute a valid token in the language.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#message)

--------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid or unexpected token (V8-based)
SyntaxError: illegal character U+201C (Firefox)
SyntaxError: Invalid character '\\u201c' (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#error_type)

--------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------

There is an invalid character that the interpreter doesn't understand. You should either put it in a string literal or replace it with another character. Use an editor that supports syntax highlighting and carefully check your code against mismatches like a minus sign (`-`) versus a dash (`–`) or simple quotes (`"`) versus non-standard quotation marks (`“`).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#examples)

----------------------------------------------------------------------------------------------------------------

### [Mismatched characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#mismatched_characters)

Some characters look similar, but will cause the parser to fail interpreting your code. Famous examples of this are quotes, the minus or semicolon ([greek question mark (U+37e)](https://en.wikipedia.org/wiki/Question_mark#Greek_question_mark "External link (opens in new tab)")
 looks same).

This should work:

Some editors and IDEs will notify you or at least use a slightly different highlighting for it, but not all. When something like this happens to your code and you're not able to find the source of the problem, it's often best to just delete the problematic line and retype it.

### [Forgotten characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#forgotten_characters)

It's easy to forget a character here or there.

Add the missing quote for `"×"`.

### [Hidden characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#hidden_characters)

When copy pasting code from external sources, there might be invalid characters. Watch out!

When inspecting this code in an editor like VIM, you can see that there is actually a [zero-width space (ZWSP) (U+200B)](https://en.wikipedia.org/wiki/Zero-width_space "External link (opens in new tab)")
 character.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Illegal_character/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/illegal_character/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/illegal_character (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FIllegal_character&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fillegal_character%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FIllegal_character%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fillegal_character%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")