*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#mdn-search)
    

const
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`const`** declaration declares block-scoped local variables. The value of a constant can't be changed through reassignment using the [assignment operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
, but if a constant is an [object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#objects)
, its properties can be added, updated, or removed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#syntax)

----------------------------------------------------------------------------------------------------

[`nameN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#namen)

The name of the variable to declare. Each must be a legal JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 or a [destructuring binding pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`valueN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#valuen)

Initial value of the variable. It can be any legal expression.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#description)

--------------------------------------------------------------------------------------------------------------

The `const` declaration is very similar to [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
:

*   `const` declarations are scoped to blocks as well as functions.
    
*   `const` declarations can only be accessed after the place of declaration is reached (see [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
    ). For this reason, `const` declarations are commonly regarded as [non-hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
    .
    
*   `const` declarations do not create properties on [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
     when declared at the top level of a script.
    
*   `const` declarations cannot be [redeclared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#redeclarations)
     by any other declaration in the same scope.
    
*   `const` begins [_declarations_, not _statements_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
    . That means you cannot use a lone `const` declaration as the body of a block (which makes sense, since there's no way to access the variable).
    

An initializer for a constant is required. You must specify its value in the same declaration. (This makes sense, given that it can't be changed later.)

The `const` declaration creates an immutable reference to a value. It does _not_ mean the value it holds is immutable — just that the variable identifier cannot be reassigned. For instance, in the case where the content is an object, this means the object's contents (e.g., its properties) can be altered. You should understand `const` declarations as "create a variable whose _identity_ remains constant", not "whose _value_ remains constant" — or, "create immutable [bindings](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
", not "immutable values".

Many style guides (including [MDN's](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript#variable_declarations)
) recommend using `const` over [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 whenever a variable is not reassigned in its scope. This makes the intent clear that a variable's type (or value, in the case of a primitive) can never change. Others may prefer `let` for non-primitives that are mutated.

The list that follows the `const` keyword is called a _[binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 list_ and is separated by commas, where the commas are _not_ [comma operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
 and the `=` signs are _not_ [assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
. Initializers of later variables can refer to earlier variables in the list.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#examples)

--------------------------------------------------------------------------------------------------------

### [Basic const usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#basic_const_usage)

Constants can be declared with uppercase or lowercase, but a common convention is to use all-uppercase letters, especially for primitives because they are truly immutable.

### [Block scoping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#block_scoping)

It's important to note the nature of block scoping.

### [const in objects and arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#const_in_objects_and_arrays)

`const` also works on objects and arrays. Attempting to overwrite the object throws an error "Assignment to constant variable".

However, object keys are not protected, so the following statement is executed without problem.

You would need to use [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
 to make an object immutable.

The same applies to arrays. Assigning a new array to the variable throws an error "Assignment to constant variable".

Still, it's possible to push items into the array and thus mutate it.

### [Declaration with destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#declaration_with_destructuring)

The left-hand side of each `=` can also be a binding pattern. This allows creating multiple variables at once.

For more information, see [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-let-and-const-declarations](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-let-and-const-declarations) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const#see_also)

--------------------------------------------------------------------------------------------------------

*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [Constants in the JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#constants)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/const/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/const (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fconst&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fconst%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fconst%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fconst%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5c8d0ac21db572edebbd4ad428efca0af3ec1734%0A*+Document+last+modified%3A+2026-09-04T17%3A06%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")