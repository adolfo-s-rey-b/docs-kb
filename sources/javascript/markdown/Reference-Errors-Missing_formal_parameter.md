*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#mdn-search)
    

SyntaxError: missing formal parameter
=====================================

The JavaScript exception "missing formal parameter" occurs when your function declaration is missing valid parameters.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#message)

---------------------------------------------------------------------------------------------------------------------

SyntaxError: missing formal parameter (Firefox)
SyntaxError: Unexpected number '3'. Expected a parameter pattern or a ')' in parameter list. (Safari)
SyntaxError: Unexpected string literal "x". Expected a parameter pattern or a ')' in parameter list. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#error_type)

---------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------------

"Formal parameter" is a fancy way of saying "function parameter". Your function declaration is missing valid parameters. In the declaration of a function, the parameters must be [identifiers](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
, not any value like numbers, strings, or objects. Declaring functions and calling functions are two separate steps. Declarations require identifier as parameters, and only when calling (invoking) the function, you provide the values the function should use.

In [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
, identifiers can contain only alphanumeric characters (or "$" or "\_"), and may not start with a digit. An identifier differs from a **string** in that a string is data, while an identifier is part of the code.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Provide proper function parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#provide_proper_function_parameters)

Function parameters must be identifiers when setting up a function. All these function declarations fail, as they are providing values for their parameters:

You will need to use identifiers in function declarations:

You can then call these functions with the arguments you like:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [SyntaxError: redeclaration of formal parameter "x"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Redeclared_parameter)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_formal_parameter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/missing_formal_parameter/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/missing_formal_parameter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_formal_parameter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_formal_parameter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_formal_parameter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_formal_parameter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")