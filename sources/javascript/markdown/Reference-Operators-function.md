*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#mdn-search)
    

function expression
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`function`** keyword can be used to define a function inside an expression.

You can also define functions using the [`function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 or the [arrow syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#try_it)

------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#syntax)

------------------------------------------------------------------------------------------------------

**Note:** An [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 cannot begin with the keyword `function` to avoid ambiguity with a [`function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
. The `function` keyword only begins an expression when it appears in a context that cannot accept statements.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#parameters)

[`name` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#name)

The function name. Can be omitted, in which case the function is _anonymous_. The name is only local to the function body.

[`paramN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#paramn)

The name of a formal parameter for the function. For the parameters' syntax, see the [Functions reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_parameters)
.

[`statements` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#statements)

The statements which comprise the body of the function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#description)

----------------------------------------------------------------------------------------------------------------

A `function` expression is very similar to, and has almost the same syntax as, a [`function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
. The main difference between a `function` expression and a `function` declaration is the _function name_, which can be omitted in `function` expressions to create _anonymous_ functions. A `function` expression can be used as an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 (Immediately Invoked Function Expression) which runs as soon as it is defined. See also the chapter about [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 for more information.

### [Function expression hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#function_expression_hoisting)

Function expressions in JavaScript are not hoisted, unlike [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#hoisting)
. You can't use function expressions before you create them:

### [Named function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#named_function_expression)

If you want to refer to the current function inside the function body, you need to create a named function expression. This name is then local only to the function body (scope). This avoids using the deprecated [`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)
 property to call the function recursively.

If a function expression is named, the [`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name)
 property of the function is set to that name, instead of the implicit name inferred from syntax (such as the variable the function is assigned to).

Unlike declarations, the name of the function expressions is read-only.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#examples)

----------------------------------------------------------------------------------------------------------

### [Using function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#using_function_expression)

The following example defines an unnamed function and assigns it to `x`. The function returns the square of its argument:

### [Using a function as a callback](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#using_a_function_as_a_callback)

More commonly it is used as a [callback](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)
:

### [Using an Immediately Invoked Function Expression (IIFE)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#using_an_immediately_invoked_function_expression_iife)

[IIFEs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 are a common pattern used to execute arbitrarily many statements in their own scope (and possibly return a value), in a location that requires a single expression. Many traditional use cases of IIFEs have been obsoleted by new syntax features such as [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
 and [block-scoped declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
. IIFEs themselves are more commonly written with [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 now, but the idea remains the same. In general, IIFEs look like this:

Here, we introduce several use cases with examples.

### [Avoid polluting the global namespace in script code](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#avoid_polluting_the_global_namespace_in_script_code)

The top-level scope of all scripts is shared, which could include many functions and global variables from different files, so to avoid name conflicts, it's important to limit the number of globally declared names (this is greatly mitigated in [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#module_philosophy)
, but sometimes limiting the scope of temporary variables is still useful, especially when the file is very long). If we have some initialization code that we don't need to use again, we could use the IIFE pattern, which is better than using a function declaration or a function expression because it ensures that the code is only run here and once.

### [The module pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#the_module_pattern)

We would also use IIFE to create private and public variables and methods. For a more sophisticated use of the module pattern and other use of IIFE, you could see the book Learning JavaScript Design Patterns by Addy Osmani.

### [For loop with var before ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#for_loop_with_var_before_es6)

We could see the following use of IIFE in some old code, before the introduction of the block-scoped `let` and `const` declarations. With the statement `var`, we have only function scopes and the global scope. Suppose we want to create 2 buttons with the texts Button 0 and Button 1 and when we click them, we would like them to alert 0 and 1. The following code doesn't work:

When clicked, both Button 0 and Button 1 alert 2 because `i` is global, with the last value 2. To fix this problem before ES6, we could use the IIFE pattern:

When clicked, Buttons 0 and 1 alert 0 and 1. The variable `i` is globally defined. Using the statement `let`, we could simply do:

When clicked, these buttons alert 0 and 1.

### [Control flow statements in expression positions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#control_flow_statements_in_expression_positions)

IIFEs enable us to use language constructs such as `switch` in an expression.

This approach can be especially useful in scenarios where you want to make a variable `const`, but are forced to use `let` or `var` during initialization:

Using IIFEs, we can make the variable `const`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function#see_also)

----------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    
*   [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/function/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Ffunction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Ffunction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Ffunction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Ffunction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")