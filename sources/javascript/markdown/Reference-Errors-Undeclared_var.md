*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#mdn-search)
    

ReferenceError: assignment to undeclared variable "x"
=====================================================

The JavaScript [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
\-only exception "Assignment to undeclared variable" occurs when the value has been assigned to an undeclared variable.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#message)

-----------------------------------------------------------------------------------------------------------

ReferenceError: x is not defined (V8-based)
ReferenceError: assignment to undeclared variable x (Firefox)
ReferenceError: Can't find variable: x (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#error_type)

-----------------------------------------------------------------------------------------------------------------

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
 in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 only.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------

You have an assignment of the form `x = ...`, but `x` has not been previously declared with the `var`, `let`, or `const` keyword. This error occurs in [strict mode code](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 only. In non-strict code, assignment to an undeclared variable implicitly creates a property on the global scope.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#examples)

-------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#invalid_cases)

In this case, the variable "bar" is an undeclared variable.

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#valid_cases)

To make "bar" a declared variable, you can add a [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, or [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
 keyword in front of it.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    
*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 18, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/undeclared_var/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/undeclared_var (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUndeclared_var&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fundeclared_var%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUndeclared_var%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fundeclared_var%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6190afbbd086e1db1158730d10a4c7896fc8f0c2%0A*+Document+last+modified%3A+2025-12-18T23%3A36%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")