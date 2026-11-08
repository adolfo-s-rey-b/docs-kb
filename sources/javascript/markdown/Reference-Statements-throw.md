*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#mdn-search)
    

throw
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`throw`** statement throws a user-defined exception. Execution of the current function will stop (the statements after `throw` won't be executed), and control will be passed to the first [`catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 block in the call stack. If no `catch` block exists among caller functions, the program will terminate.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#syntax)

----------------------------------------------------------------------------------------------------

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#expression)

The expression to throw.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#description)

--------------------------------------------------------------------------------------------------------------

The `throw` statement is valid in all contexts where statements can be used. Its execution generates an exception that penetrates through the call stack. For more information on error bubbling and handling, see [Control flow and error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
.

The `throw` keyword can be followed by any kind of expression, for example:

In practice, the exception you throw should _always_ be an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 object or an instance of an `Error` subclass, such as [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
. This is because code that catches the error may expect certain properties, such as [`message`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/message)
, to be present on the caught value. For example, web APIs typically throw [`DOMException`](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
 instances, which inherit from `Error.prototype`.

### [Automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#automatic_semicolon_insertion)

The syntax forbids line terminators between the `throw` keyword and the expression to be thrown.

The code above is transformed by [automatic semicolon insertion (ASI)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 into:

This is invalid code, because unlike [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
, `throw` must be followed by an expression.

To avoid this problem (to prevent ASI), you could use parentheses:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#examples)

--------------------------------------------------------------------------------------------------------

### [Throwing a user-defined error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#throwing_a_user-defined_error)

This example defines a function that throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if the input is not of the expected type.

### [Throwing an existing object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#throwing_an_existing_object)

This example calls a callback-based async function, and throws an error if the callback receives an error.

Errors thrown this way are not catchable by the caller and will cause the program to crash unless (a) the `readFile` function itself catches the error, or (b) the program is running in a context that catches top-level errors. You can handle errors more naturally by using the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-throw-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-throw-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw#see_also)

--------------------------------------------------------------------------------------------------------

*   [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    
*   [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/throw/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/throw (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fthrow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fthrow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fthrow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fthrow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")