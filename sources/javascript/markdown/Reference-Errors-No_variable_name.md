*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#mdn-search)
    

SyntaxError: missing variable name
==================================

The JavaScript exception "missing variable name" is a common error. It is usually caused by omitting a variable name or a typographic error.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#message)

-------------------------------------------------------------------------------------------------------------

SyntaxError: missing variable name (Firefox)
SyntaxError: Unexpected token '='. Expected a parameter pattern or a ')' in parameter list. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#error_type)

-------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------

A variable is missing a name. The cause is most likely a typo or a forgotten variable name. Make sure that you've provided the name of the variable before the `=` sign.

When declaring multiple variables at the same time, make sure that the previous lines/declaration does not end with a comma instead of a semicolon.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#examples)

---------------------------------------------------------------------------------------------------------------

### [Missing a variable name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#missing_a_variable_name)

It is easy to forget to assign a name for your variable!

### [Reserved keywords can't be variable names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#reserved_keywords_cant_be_variable_names)

There are a few variable names that are [reserved keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
. You can't use these. Sorry :(

### [Declaring multiple variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#declaring_multiple_variables)

Pay special attention to commas when declaring multiple variables. Is there an excess comma, or did you use commas instead of semicolons? Did you remember to assign values for all your `const` variables?

The fixed version:

### [Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#arrays)

[`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 literals in JavaScript need square brackets around the values. This won't work:

This would be correct:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    
*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    
*   [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/No_variable_name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/no_variable_name/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/no_variable_name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNo_variable_name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fno_variable_name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNo_variable_name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fno_variable_name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")