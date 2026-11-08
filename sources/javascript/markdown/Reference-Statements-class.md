*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#mdn-search)
    

class
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`class`** declaration creates a [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 of a new [class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 to a given name.

You can also define classes using the [`class` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#syntax)

----------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#description)

--------------------------------------------------------------------------------------------------------------

The class body of a class declaration is executed in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. The `class` declaration is very similar to [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
:

*   `class` declarations are scoped to blocks as well as functions.
*   `class` declarations can only be accessed after the place of declaration is reached (see [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
    ). For this reason, `class` declarations are commonly regarded as [non-hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
     (unlike [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    ).
*   `class` declarations do not create properties on [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
     when declared at the top level of a script (unlike [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    ).
*   `class` declarations cannot be [redeclared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#redeclarations)
     by any other declaration in the same scope.

Outside the class body, `class` declarations can be re-assigned like `let`, but you should avoid doing so. Within the class body, the binding is constant like `const`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#examples)

--------------------------------------------------------------------------------------------------------

### [A class declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#a_class_declaration)

In the following example, we first define a class named `Rectangle`, then extend it to create a class named `FilledRectangle`.

Note that `super()`, used in the `constructor`, can only be used in constructors, and _must_ be called _before_ the `this` keyword can be used.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class#see_also)

--------------------------------------------------------------------------------------------------------

*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`class` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
    
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/class/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/class (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fclass&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fclass%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fclass%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fclass%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")