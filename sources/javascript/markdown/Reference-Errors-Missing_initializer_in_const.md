*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#mdn-search)
    

SyntaxError: missing = in const declaration
===========================================

The JavaScript exception "missing = in const declaration" occurs when a const declaration was not given a value in the same statement (like `const RED_FLAG;`). You need to provide one (`const RED_FLAG = true`).

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#message)

-------------------------------------------------------------------------------------------------------------------------

SyntaxError: Missing initializer in const declaration (V8-based)
SyntaxError: missing = in const declaration (Firefox)
SyntaxError: Unexpected token ';'. const declared variable 'x' must have an initializer. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#error_type)

-------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------------

A constant is a value that cannot be altered by the program during normal execution. It cannot change through re-assignment, and it can't be redeclared. In JavaScript, constants are declared using the [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
 keyword. An initializer for a constant is required; that is, you must specify its value in the same statement in which it's declared (which makes sense, given that it can't be changed later).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Missing const initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#missing_const_initializer)

Unlike `var` or `let`, you must specify a value for a `const` declaration. This throws:

### [Fixing the error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#fixing_the_error)

There are multiple options to fix this error. Check what was intended to be achieved with the constant in question.

#### Adding a constant value

Specify the constant value in the same statement in which it's declared:

#### `const`, `let` or `var`?

Do not use `const` if you weren't meaning to declare a constant. Maybe you meant to declare a block-scoped variable with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 or global variable with [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
. Both don't require an initial value.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_initializer_in_const/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/missing_initializer_in_const/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/missing_initializer_in_const (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_initializer_in_const&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_initializer_in_const%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_initializer_in_const%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_initializer_in_const%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f2a755c4fa7d126f85b56fbca90b15c5f039eff%0A*+Document+last+modified%3A+2025-08-08T16%3A55%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")