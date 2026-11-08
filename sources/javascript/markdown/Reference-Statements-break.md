*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#mdn-search)
    

break
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`break`** statement terminates the current loop or [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
 statement and transfers program control to the statement following the terminated statement. It can also be used to jump past a [labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 when used within that labeled statement.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#syntax)

----------------------------------------------------------------------------------------------------

[`label` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#label)

Identifier associated with the label of the statement to break to. If the `break` statement is not nested within a loop or [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
, then the label identifier is required.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#description)

--------------------------------------------------------------------------------------------------------------

When `break;` is encountered, the program breaks out of the innermost `switch` or [looping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#iterations)
 statement and continues executing the next statement after that.

When `break label;` is encountered, the program breaks out of the statement labeled with `label` and continues executing the next statement after that. The `break` statement needs to be nested within the referenced label. The labeled statement can be any statement (commonly a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 statement); it does not have to be another loop statement.

A `break` statement, with or without a following label, cannot be used at the top level of a script, module, function's body, or [static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
, even when the function or class is further contained within a loop.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#examples)

--------------------------------------------------------------------------------------------------------

### [break in while loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#break_in_while_loop)

The following function has a `break` statement that terminates the [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 loop when `i` is 3, and then returns the value `3 * x`.

### [break in switch statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#break_in_switch_statements)

The following code has a `break` statement that terminates the [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
 statement when a case is matched and the corresponding code has run.

### [break in labeled blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#break_in_labeled_blocks)

The following code uses `break` statements with labeled blocks. By using `break outerBlock`, control is transferred to the end of the block statement marked as `outerBlock`.

### [Unsyntactic break statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#unsyntactic_break_statements)

A `break` statement must be nested within any label it references. The following code also uses `break` statements with labeled blocks, but generates a syntax error because its `break` statement references `block2` but it's not nested within `block2`.

Syntax errors are also generated in the following code examples which use `break` statements within functions that are nested within a loop, or labeled block that the `break` statements are intended to break out of.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-break-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-break-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break#see_also)

--------------------------------------------------------------------------------------------------------

*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    
*   [label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
    
*   [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/break/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fbreak&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fbreak%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fbreak%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fbreak%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")