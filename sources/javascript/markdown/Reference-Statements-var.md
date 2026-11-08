*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#mdn-search)
    

var
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`var`** statement declares function-scoped or globally-scoped variables, optionally initializing each to a value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#syntax)

--------------------------------------------------------------------------------------------------

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#namen)

The name of the variable to declare. Each must be a legal JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 or a [destructuring binding pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`valueN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#valuen)

Initial value of the variable. It can be any legal expression. Default value is `undefined`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#description)

------------------------------------------------------------------------------------------------------------

The scope of a variable declared with `var` is one of the following curly-brace-enclosed syntaxes that most closely contains the `var` statement:

*   Function body
*   [Static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    

Or if none of the above applies:

*   The current [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    , for code running in module mode
*   The global scope, for code running in script mode.

Importantly, other block constructs, including [block statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
, [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
, [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
, headers of [one of the `for` statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#iterations)
, do not create scopes for `var`, and variables declared with `var` inside such a block can continue to be referenced outside the block.

In a script, a variable declared using `var` is added as a non-configurable property of the global object. This means its property descriptor cannot be changed and it cannot be deleted using [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
. JavaScript has automatic memory management, and it would make no sense to be able to use the `delete` operator on a global variable.

In both Node.js [CommonJS](https://wiki.commonjs.org/wiki/CommonJS "External link (opens in new tab)")
 modules and native [ECMAScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
, top-level variable declarations are scoped to the module, and are not added as properties to the global object.

The list that follows the `var` keyword is called a _[binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 list_ and is separated by commas, where the commas are _not_ [comma operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
 and the `=` signs are _not_ [assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
. Initializers of later variables can refer to earlier variables in the list and get the initialized value.

### [Hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#hoisting)

`var` declarations, wherever they occur in a script, are processed before any code within the script is executed. Declaring a variable anywhere in the code is equivalent to declaring it at the top. This also means that a variable can appear to be used before it's declared. This behavior is called [_hoisting_](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
, as it appears that the variable declaration is moved to the top of the function, static initialization block, or script source in which it occurs.

**Note:** `var` declarations are only hoisted to the top of the current script. If you have two `<script>` elements within one HTML, the first script cannot access variables declared by the second before the second script has been processed and executed.

This is implicitly understood as:

For that reason, it is recommended to always declare variables at the top of their scope (the top of global code and the top of function code) so it's clear which variables are scoped to the current function.

Only a variable's declaration is hoisted, not its initialization. The initialization happens only when the assignment statement is reached. Until then the variable remains `undefined` (but declared):

This is implicitly understood as:

### [Redeclarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#redeclarations)

Duplicate variable declarations using `var` will not trigger an error, even in strict mode, and the variable will not lose its value, unless the declaration has an initializer.

`var` declarations can also be in the same scope as a `function` declaration. Both the function declaration and the `var` declaration are hoisted to the top, so the function value is only accessible from the start of its scope until the variable's initializer or first assignment, regardless of the two declarations' relative positions in the source code.

`var` declarations cannot be in the same scope as a [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
, or [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declaration.

Because `var` declarations are not scoped to blocks, this also applies to the following case:

It does not apply to the following case, where `let` is in a child scope of `var`, not the same scope:

A `var` declaration within a function's body can have the same name as a parameter.

A `var` declaration within a `catch` block can have the same name as the `catch`\-bound identifier, but only if the `catch` binding is a simple identifier, not a destructuring pattern. This is a [deprecated syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#statements)
 and you should not rely on it. In this case, the declaration is hoisted to outside the `catch` block, but any value assigned within the `catch` block is not visible outside.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#examples)

------------------------------------------------------------------------------------------------------

### [Declaring and initializing two variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#declaring_and_initializing_two_variables)

### [Assigning two variables with single string value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#assigning_two_variables_with_single_string_value)

This is equivalent to:

Be mindful of the order:

Here, `x` and `y` are declared before any code is executed, but the assignments occur later. At the time `x = y` is evaluated, `y` exists so no `ReferenceError` is thrown and its value is `undefined`. So, `x` is assigned the undefined value. Then, `y` is assigned the value `"A"`.

### [Initialization of several variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#initialization_of_several_variables)

Be careful of the `var x = y = 1` syntax — `y` is not actually declared as a variable, so `y = 1` is an [unqualified identifier assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#unqualified_identifier_assignment)
, which creates a global variable in non-strict mode.

The same example as above but with a strict mode:

### [Implicit globals and outer function scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#implicit_globals_and_outer_function_scope)

Variables that appear to be implicit globals may be references to variables in an outer function scope:

### [Declaration with destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#declaration_with_destructuring)

The left-hand side of each `=` can also be a binding pattern. This allows creating multiple variables at once.

For more information, see [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-variable-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-variable-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#see_also)

------------------------------------------------------------------------------------------------------

*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/var/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/var (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fvar&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fvar%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fvar%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fvar%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F710372d69095aaeadfba6c892f3e39ed63df4c54%0A*+Document+last+modified%3A+2026-08-27T09%3A56%3A24.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")