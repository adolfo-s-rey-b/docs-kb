*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#mdn-search)
    

class expression
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`class`** keyword can be used to define a class inside an expression.

You can also define classes using the [`class` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#syntax)

---------------------------------------------------------------------------------------------------

**Note:** An [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 cannot begin with the keyword `class` to avoid ambiguity with a [`class` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
. The `class` keyword only begins an expression when it appears in a context that cannot accept statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#description)

-------------------------------------------------------------------------------------------------------------

A `class` expression is very similar to, and has almost the same syntax as, a [`class` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
. As with `class` declarations, the body of a `class` expression is executed in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. The main difference between a `class` expression and a `class` declaration is the _class name_, which can be omitted in `class` expressions to create _anonymous_ classes. Class expressions allow you to redefine classes, while redeclaring a class using `class` declarations throws a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
. See also the chapter about [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 for more information.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#examples)

-------------------------------------------------------------------------------------------------------

### [A basic class expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#a_basic_class_expression)

This is just an anonymous class expression which you can refer to using the variable `Foo`.

### [Named class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#named_class_expressions)

If you want to refer to the current class inside the class body, you can create a _named class expression_. The name is only visible within the scope of the class expression itself.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class#see_also)

-------------------------------------------------------------------------------------------------------

*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/class/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/class (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fclass&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fclass%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fclass%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fclass%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")