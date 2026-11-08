*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#mdn-search)
    

SyntaxError: identifier starts immediately after numeric literal
================================================================

The JavaScript exception "identifier starts immediately after numeric literal" occurs when an identifier started with a digit. Identifiers can only start with a letter, underscore (\_), or dollar sign ($).

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#message)

--------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid or unexpected token (V8-based)
SyntaxError: identifier starts immediately after numeric literal (Firefox)
SyntaxError: No identifiers allowed directly after numeric literal (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#error_type)

--------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------

The names of variables, called [identifiers](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
, conform to certain rules, which your code must adhere to!

A JavaScript identifier must start with a letter, underscore (\_), or dollar sign ($). They can't start with a digit! Only subsequent characters can be digits (0-9).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#examples)

----------------------------------------------------------------------------------------------------------------------

### [Variable names starting with numeric literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#variable_names_starting_with_numeric_literals)

Variable names can't start with numbers in JavaScript. The following fails:

You will need to rename your variable to avoid the leading number.

In JavaScript, there is a syntactic peculiarity when calling properties or methods on numbers. If you want to call a method on an integer, you cannot immediately use a dot after the number because the dot is interpreted as the start of a decimal fraction, causing the parser to see the method's name as an identifier immediately after a number literal. To avoid this, you need to either wrap the number in parentheses or use a double dot, where the first dot is a decimal point for the number literal and the second dot is the property accessor.

Correct ways to call methods on numbers:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    
*   [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Identifier_after_number/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/identifier_after_number/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/identifier_after_number (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FIdentifier_after_number&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fidentifier_after_number%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FIdentifier_after_number%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fidentifier_after_number%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")