*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#mdn-search)
    

Inequality (!=)
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **inequality (`!=`)** operator checks whether its two operands are not equal, returning a Boolean result. Unlike the [strict inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
 operator, it attempts to convert and compare operands that are of different types.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#try_it)

--------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#syntax)

--------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#description)

------------------------------------------------------------------------------------------------------------------

The inequality operator checks whether its operands are not equal. It is the negation of the [equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 operator so the following two lines will always give the same result:

For details of the comparison algorithm, see the page for the [equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 operator.

Like the equality operator, the inequality operator will attempt to convert and compare operands of different types:

To prevent this, and require that different types are considered to be different, use the [strict inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
 operator instead:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#examples)

------------------------------------------------------------------------------------------------------------

### [Comparison with no type conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#comparison_with_no_type_conversion)

### [Comparison with type conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#comparison_with_type_conversion)

### [Comparison of objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#comparison_of_objects)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-equality-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-equality-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality#see_also)

------------------------------------------------------------------------------------------------------------

*   [Equality (`==`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
    
*   [Strict equality (`===`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
    
*   [Strict inequality (`!==`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/inequality/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/inequality (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FInequality&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Finequality%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FInequality%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Finequality%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")