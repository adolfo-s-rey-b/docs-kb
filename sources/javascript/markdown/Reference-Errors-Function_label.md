*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#mdn-search)
    

SyntaxError: functions cannot be labelled
=========================================

The JavaScript exception "functions cannot be labelled" occurs when a [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 declaration has a [label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 before it.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#message)

-----------------------------------------------------------------------------------------------------------

SyntaxError: In non-strict mode code, functions can only be declared at top level, inside a block, or as the body of an if statement. (V8-based)
SyntaxError: In strict mode code, functions can only be declared at top level or inside a block. (V8-based)
SyntaxError: Generators can only be declared at the top level or inside a block. (V8-based)
SyntaxError: Async functions can only be declared at the top level or inside a block. (V8-based)

SyntaxError: functions can only be labelled inside blocks (Firefox)
SyntaxError: functions cannot be labelled (Firefox)
SyntaxError: generator functions cannot be labelled (Firefox)
SyntaxError: async function declarations can't appear in single-statement context (Firefox)

SyntaxError: Unexpected keyword 'function'. Function declarations are only allowed inside block statements or at the top level of a program. (Safari)
SyntaxError: Function declarations are only allowed inside blocks or switch statements in strict mode. (Safari)
SyntaxError: Unexpected token '\*'. Cannot use generator function declaration in single-statement context. (Safari)
SyntaxError: Unexpected keyword 'function'. Cannot use async function declaration in single-statement context. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#error_type)

-----------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------

Function declarations are never supposed to be labeled, because labels should only apply to statements, not declarations. There's no way to actually jump to this label. However, due to some legacy JavaScript syntax rules, the error condition is a bit more complicated than necessary:

*   In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    , function declarations are never allowed to be labeled.
*   In non-strict mode, function declarations are allowed to be labeled, but not when the function is the sole statement of an `if` statement (which itself is a deprecated feature).
*   Async functions, generator functions, and async generator functions are never allowed to be labeled.

The error message may say something along the lines of "invalid place for a function declaration to appear", because when the parser sees a label, it expects a statement to follow, and a function declaration is not a statement. It depends on whether the error's perspective is that a label cannot be followed by a function, or that a function cannot be preceded by a label.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#examples)

-------------------------------------------------------------------------------------------------------------

### [Misparsed object literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#misparsed_object_literal)

While it's possible that you actually expect the label to do _something_ along the lines of being a jump target, usually you didn't intend for it to be a label. The most common case is you actually want it to be a property key in an object literal:

Here, `{...}` is actually not an object literal, but is instead the block body of the [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
, so `greet:` becomes a label. To fix this, you need to wrap the object literal in parentheses:

You may also want to use the [method syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
 for object literals, which avoids this pitfall:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
    
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    
*   [Deprecated and obsolete features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Function_label/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/function_label/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/function_label (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FFunction_label&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Ffunction_label%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FFunction_label%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Ffunction_label%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F65692fd4d256d5647749b7c7005dcf53d425a533%0A*+Document+last+modified%3A+2026-08-27T19%3A48%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")