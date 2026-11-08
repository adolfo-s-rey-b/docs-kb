*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#mdn-search)
    

let
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`let`** declaration declares re-assignable, block-scoped local variables, optionally initializing each to a value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#syntax)

--------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#parameters)

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#namen)

The name of the variable to declare. Each must be a legal JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 or a [destructuring binding pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`valueN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#valuen)

Initial value of the variable. It can be any legal expression. Default value is `undefined`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#description)

------------------------------------------------------------------------------------------------------------

The scope of a variable declared with `let` is one of the following curly-brace-enclosed syntaxes that most closely contains the `let` declaration:

*   [Block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
     statement
*   [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
     statement
*   [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
     statement
*   Body of [one of the `for` statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#iterations)
    , if the `let` is in the header of the statement
*   Function body
*   [Static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    

Or if none of the above applies:

*   The current [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    , for code running in module mode
*   The global scope, for code running in script mode.

Compared with [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, `let` declarations have the following differences:

*   `let` declarations are scoped to blocks as well as functions.
    
*   `let` declarations can only be accessed after the place of declaration is reached (see [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
    ). For this reason, `let` declarations are commonly regarded as [non-hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
    .
    
*   `let` declarations do not create properties on [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
     when declared at the top level of a script.
    
*   `let` declarations cannot be [redeclared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#redeclarations)
     by any other declaration in the same scope.
    
*   `let` begins [_declarations_, not _statements_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
    . That means you cannot use a lone `let` declaration as the body of a block (which makes sense, since there's no way to access the variable).
    

Note that `let` is allowed as an identifier name when declared with `var` or `function` in [non-strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, but you should avoid using `let` as an identifier name to prevent unexpected syntax ambiguities.

Many style guides (including [MDN's](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript#variable_declarations)
) recommend using [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
 over `let` whenever a variable is not reassigned in its scope. This makes the intent clear that a variable's type (or value, in the case of a primitive) can never change. Others may prefer `let` for non-primitives that are mutated.

The list that follows the `let` keyword is called a _[binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 list_ and is separated by commas, where the commas are _not_ [comma operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
 and the `=` signs are _not_ [assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
. Initializers of later variables can refer to earlier variables in the list.

### [Temporal dead zone (TDZ)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)

A variable declared with `let`, `const`, or `class` is said to be in a "temporal dead zone" (TDZ) from the start of the block until code execution reaches the place where the variable is declared and initialized.

While inside the TDZ, the variable has not been initialized with a value, and any attempt to access it will result in a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
. The variable is initialized with a value when execution reaches the place in the code where it was declared. If no initial value was specified with the variable declaration, it will be initialized with a value of `undefined`.

This differs from [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#hoisting)
 variables, which will return a value of `undefined` if they are accessed before they are declared. The code below demonstrates the different result when `let` and `var` are accessed in code before the place where they are declared.

The term "temporal" is used because the zone depends on the order of execution (time) rather than the order in which the code is written (position). For example, the code below works because, even though the function that uses the `let` variable appears before the variable is declared, the function is _called_ outside the TDZ.

Using the `typeof` operator for a variable in its TDZ will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
:

This differs from using `typeof` for undeclared variables, and variables that hold a value of `undefined`:

**Note:** `let` and `const` declarations are only processed when the current script gets processed. If you have two `<script>` elements running in script mode within one HTML, the first script is not subject to the TDZ restrictions for top-level `let` or `const` variables declared in the second script, although if you declare a `let` or `const` variable in the first script, declaring it again in the second script will cause a [redeclaration error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#redeclarations)
.

### [Redeclarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#redeclarations)

`let` declarations cannot be in the same scope as any other declaration, including `let`, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
, [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
, [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, and [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declaration.

A `let` declaration within a function's body cannot have the same name as a parameter. A `let` declaration within a `catch` block cannot have the same name as the `catch`\-bound identifier.

If you're experimenting in a REPL, such as the Firefox web console (**Tools** > **Web Developer** > **Web Console**), and you run two `let` declarations with the same name in two separate inputs, you may get the same re-declaration error. See further discussion of this issue in [Firefox bug 1580891](https://bugzil.la/1580891 "External link (opens in new tab)")
. The Chrome console allows `let` re-declarations between different REPL inputs.

You may encounter errors in [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
 statements because there is only one block.

To avoid the error, wrap each `case` in a new block statement.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#examples)

------------------------------------------------------------------------------------------------------

### [Scoping rules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#scoping_rules)

Variables declared by `let` have their scope in the block for which they are declared, as well as in any contained sub-blocks. In this way, `let` works very much like `var`. The main difference is that the scope of a `var` variable is the entire enclosing function:

At the top level of programs and functions, `let`, unlike `var`, does not create a property on the global object. For example:

### [TDZ combined with lexical scoping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#tdz_combined_with_lexical_scoping)

The following code results in a `ReferenceError` at the line shown:

The `if` block is evaluated because the outer `var foo` has a value. However due to lexical scoping this value is not available inside the block: the identifier `foo` _inside_ the `if` block is the `let foo`. The expression `foo + 55` throws a `ReferenceError` because initialization of `let foo` has not completed — it is still in the temporal dead zone.

This phenomenon can be confusing in a situation like the following. The instruction `let n of n.a` is already inside the scope of the `for...of` loop's block. So, the identifier `n.a` is resolved to the property `a` of the `n` object located in the first part of the instruction itself (`let n`). This is still in the temporal dead zone as its declaration statement has not been reached and terminated.

### [Other situations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#other_situations)

When used inside a block, `let` limits the variable's scope to that block. Note the difference between `var`, whose scope is inside the function where it is declared.

However, this combination of `var` and `let` declarations below is a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 because `var` not being block-scoped, leading to them being in the same scope. This results in an implicit re-declaration of the variable.

### [Declaration with destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#declaration_with_destructuring)

The left-hand side of each `=` can also be a binding pattern. This allows creating multiple variables at once.

For more information, see [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-let-and-const-declarations](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-let-and-const-declarations) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#see_also)

------------------------------------------------------------------------------------------------------

*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
    
*   [ES6 In Depth: `let` and `const`](https://hacks.mozilla.org/2015/07/es6-in-depth-let-and-const/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)
*   [Breaking changes in `let` and `const` in Firefox 44](https://blog.mozilla.org/addons/2015/10/14/breaking-changes-let-const-firefox-nightly-44/ "External link (opens in new tab)")
     on blog.mozilla.org (2015)
*   [You Don't Know JS: Scope & Closures, Ch.3: Function vs. Block Scope](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/scope%20%26%20closures/ch3.md "External link (opens in new tab)")
     by Kyle Simpson
*   [What is the Temporal Dead Zone?](https://stackoverflow.com/questions/33198849/what-is-the-temporal-dead-zone/33198850 "External link (opens in new tab)")
     on Stack Overflow
*   [What is the difference between using `let` and `var`?](https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var "External link (opens in new tab)")
     on Stack Overflow
*   [Why was the name 'let' chosen for block-scoped variable declarations in JavaScript?](https://stackoverflow.com/questions/37916940/why-was-the-name-let-chosen-for-block-scoped-variable-declarations-in-javascri "External link (opens in new tab)")
     on Stack Overflow

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/let/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/let (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Flet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Flet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Flet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Flet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5c8d0ac21db572edebbd4ad428efca0af3ec1734%0A*+Document+last+modified%3A+2026-09-04T17%3A06%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")