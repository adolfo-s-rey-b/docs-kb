*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#mdn-search)
    

ReferenceError: "x" is not defined
==================================

The JavaScript exception "_variable_ is not defined" occurs when there is a non-existent variable referenced somewhere.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#message)

--------------------------------------------------------------------------------------------------------

ReferenceError: "x" is not defined (V8-based & Firefox)
ReferenceError: Can't find variable: x (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#error_type)

--------------------------------------------------------------------------------------------------------------

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------

There is a non-existent variable referenced somewhere. This variable needs to be declared, or you need to make sure it is available in your current script or [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
.

**Note:** When loading a library (such as jQuery), make sure it is loaded before you access library variables, such as "$". Put the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element that loads the library before your code that uses it.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#examples)

----------------------------------------------------------------------------------------------------------

### [Variable not declared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#variable_not_declared)

js

    foo.substring(1); // ReferenceError: foo is not defined
    

The "foo" variable isn't defined anywhere. It needs to be some string, so that the [`String.prototype.substring()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
 method will work.

js

    const foo = "bar";
    foo.substring(1); // "ar"
    

### [Wrong scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#wrong_scope)

A variable needs to be available in the current context of execution. Variables defined inside a [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 cannot be accessed from anywhere outside the function, because the variable is defined only in the scope of the function

js

    function numbers() {
      const num1 = 2;
      const num2 = 3;
      return num1 + num2;
    }
    
    console.log(num1); // ReferenceError num1 is not defined.
    

However, a function can access all variables and functions defined inside the scope in which it is defined. In other words, a function defined in the global scope can access all variables defined in the global scope.

js

    const num1 = 2;
    const num2 = 3;
    
    function numbers() {
      return num1 + num2;
    }
    
    console.log(numbers()); // 5
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined#see_also)

----------------------------------------------------------------------------------------------------------

*   [Scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
    
*   [Declaring variables in the JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#declaring_variables)
    
*   [Function scope in the JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_scopes_and_closures)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/not_defined/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/not_defined (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNot_defined&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fnot_defined%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FNot_defined%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fnot_defined%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")