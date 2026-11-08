*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#mdn-search)
    

SyntaxError: reference to undeclared private field or method #x
===============================================================

The JavaScript exception "reference to undeclared private field or method #x" occurs when a [private name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 is used, but this private name is not declared in the class scope.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#message)

-------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Private field '#x' must be declared in an enclosing class (V8-based)
SyntaxError: reference to undeclared private field or method #x (Firefox)
SyntaxError: Cannot reference undeclared private names: "#x" (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#error_type)

-------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------------------

Unlike normal string or symbol properties, which return `undefined` if the property does not exist, private names are very strict and can only be legally accessed if they actually exist. Accessing an undeclared private name will result in a syntax error, while accessing a private name that is declared but doesn't exist on the object will result in a [type error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Get_set_missing_private)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#examples)

---------------------------------------------------------------------------------------------------------------------------------

### [Undeclared private field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#undeclared_private_field)

You cannot access a private field that is not declared in the class scope.

The same error occurs if you use the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator to perform a check on an undeclared private field.

These code are probably mistakes because it's impossible for `#x` to exist on `this` if it's not declared in the class scope. Note that you cannot dynamically _add_ private elements to unrelated objects. You should either remove this code or declare the private field in the class scope.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method#see_also)

---------------------------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_private_field_or_method/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/undeclared_private_field_or_method/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/undeclared_private_field_or_method (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUndeclared_private_field_or_method&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fundeclared_private_field_or_method%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUndeclared_private_field_or_method%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fundeclared_private_field_or_method%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")