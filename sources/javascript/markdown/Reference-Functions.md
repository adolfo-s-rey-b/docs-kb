*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#mdn-search)
    

Functions
=========

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

Generally speaking, a function is a "subprogram" that can be _called_ by code external (or internal, in the case of recursion) to the function. Like the program itself, a function is composed of a sequence of statements called the _function body_. Values can be _passed_ to a function as parameters, and the function will _return_ a value.

In JavaScript, functions are [first-class objects](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)
, because they can be passed to other functions, returned from functions, and assigned to variables and properties. They can also have properties and methods just like any other object. What distinguishes them from other objects is that functions can be called.

For more examples and explanations, see the [JavaScript guide about functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#description)

-------------------------------------------------------------------------------------------------------

Function values are typically instances of [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
. See [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 for information on properties and methods of `Function` objects. Callable values cause [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 to return `"function"` instead of `"object"`.

**Note:** Not all callable values are `instanceof Function`. For example, the `Function.prototype` object is callable but not an instance of `Function`. You can also manually set the [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 of your function so it no longer inherits from `Function.prototype`. However, such cases are extremely rare.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#return_value)

By default, if a function's execution doesn't end at a [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement, or if the `return` keyword doesn't have an expression after it, then the return value is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. The `return` statement allows you to return an arbitrary value from the function. One function call can only return one value, but you can simulate the effect of returning multiple values by returning an object or array and [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 the result.

**Note:** Constructors called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 have a different set of logic to determine their return values.

### [Passing arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#passing_arguments)

[Parameters and arguments](https://en.wikipedia.org/wiki/Parameter_(computer_programming)#Parameters_and_arguments "External link (opens in new tab)")
 have slightly different meanings, but in MDN web docs, we often use them interchangeably. For a quick reference:

In this example, the `num` variable is called the function's _parameter_: it's declared in the parenthesis-enclosed list of the function's definition. The function expects the `num` parameter to be a number — although this is not enforceable in JavaScript without writing runtime validation code. In the `formatNumber(2)` call, the number `2` is the function's _argument_: it's the value that is actually passed to the function in the function call. The argument value can be accessed inside the function body through the corresponding parameter name or the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object.

Arguments are always [_passed by value_](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_value "External link (opens in new tab)")
 and never [_passed by reference_](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_reference "External link (opens in new tab)")
. This means that if a function reassigns a parameter, the value won't change outside the function. More precisely, object arguments are [_passed by sharing_](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing "External link (opens in new tab)")
, which means if the object's properties are mutated, the change will impact the outside of the function. For example:

The [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 keyword refers to the object that the function is accessed on — it does not refer to the currently executing function, so you must refer to the function value by name, even within the function body.

### [Defining functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#defining_functions)

Broadly speaking, JavaScript has four kinds of functions:

*   Regular function: can return anything; always runs to completion after invocation
*   Generator function: returns a [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
     object; can be paused and resumed with the [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
     operator
*   Async function: returns a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    ; can be paused and resumed with the [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
     operator
*   Async generator function: returns an [`AsyncGenerator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
     object; both the `await` and `yield` operators can be used

For every kind of function, there are multiple ways to define it:

[Declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#declaration)

[`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
, [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
, [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
, [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)

[Expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#expression)

[`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
, [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
, [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function)
, [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function*)

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#constructor)

[`Function()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
, [`GeneratorFunction()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction)
, [`AsyncFunction()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction/AsyncFunction)
, [`AsyncGeneratorFunction()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/AsyncGeneratorFunction)

In addition, there are special syntaxes for defining [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 and [methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
, which provide more precise semantics for their usage. [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 are conceptually not functions (because they throw an error when called without `new`), but they also inherit from `Function.prototype` and have `typeof MyClass === "function"`.

All syntaxes do approximately the same thing, but there are some subtle behavior differences.

*   The `Function()` constructor, `function` expression, and `function` declaration syntaxes create full-fledged function objects, which can be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    . However, arrow functions and methods cannot be constructed. Async functions, generator functions, and async generator functions are not constructible regardless of syntax.
*   The `function` declaration creates functions that are [_hoisted_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_hoisting)
    . Other syntaxes do not hoist the function and the function value is only visible after the definition.
*   The arrow function and `Function()` constructor always create _anonymous_ functions, which means they can't easily call themselves recursively. One way to call an arrow function recursively is by assigning it to a variable.
*   The arrow function syntax does not create its own bindings for `arguments` or `this`.
*   The `Function()` constructor cannot access any local variables — it only has access to the global scope.
*   The `Function()` constructor causes runtime compilation and is often slower than other syntaxes.

For `function` expressions, there is a distinction between the function name and the variable the function is assigned to. The function name cannot be changed, while the variable the function is assigned to can be reassigned. The function name can be different from the variable the function is assigned to — they have no relation to each other. The function name can be used only within the function's body. Attempting to use it outside the function's body results in an error (or gets another value, if the same name is declared elsewhere). For example:

On the other hand, the variable the function is assigned to is limited only by its scope, which is guaranteed to include the scope in which the function is declared.

A function declaration also creates a variable with the same name as the function name. Thus, unlike those defined by function expressions, functions defined by function declarations can be accessed by their name in the scope they were defined in, as well as in their own body.

A function defined by `new Function` will dynamically have its source assembled, which is observable when you serialize it. For example, `console.log(new Function().toString())` gives:

This is the actual source used to compile the function. However, although the `Function()` constructor will create the function with name `anonymous`, this name is not added to the scope of the body. The body only ever has access to global variables. For example, the following would result in an error:

A function defined by a function expression or by a function declaration inherits the current scope. That is, the function forms a closure. On the other hand, a function defined by a `Function` constructor does not inherit any scope other than the global scope (which all functions inherit).

Functions defined by function expressions and function declarations are parsed only once, while a function defined by the `Function` constructor parses the string passed to it each and every time the constructor is called. Although a function expression creates a closure every time, the function body is not reparsed, so function expressions are still faster than `new Function(...)`. Therefore the `Function` constructor should generally be avoided whenever possible.

A function declaration may be unintentionally turned into a function expression when it appears in an expression context.

On the other hand, a function expression may also be turned into a function declaration. An [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 cannot begin with the `function` or `async function` keywords, which is a common mistake when implementing [IIFEs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 (Immediately Invoked Function Expressions).

Instead, start the expression statement with something else, so that the `function` keyword unambiguously starts a function expression. Common options include [grouping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)
 and using [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
.

### [Function parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#function_parameters)

Each function parameter is a simple identifier that you can access in the local scope.

There are three special parameter syntaxes:

*   [_Default parameters_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
     allow formal parameters to be initialized with default values if no value or `undefined` is passed.
*   The [_rest parameter_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
     allows representing an indefinite number of arguments as an array.
*   [_Destructuring_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
     allows unpacking elements from arrays, or properties from objects, into distinct variables.

There are some consequences if one of the above non-simple parameter syntaxes is used:

*   You cannot apply `"use strict"` to the function body — this causes a [syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Strict_non_simple_params)
    .
*   Even if the function is not in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    , certain strict mode function features apply, including that the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
     object stops syncing with the named parameters, [`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)
     throws an error when accessed, and duplicate parameter names are not allowed.

### [The arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#the_arguments_object)

You can refer to a function's arguments within the function by using the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object.

[`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)

An array-like object containing the arguments passed to the currently executing function.

[`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)

The currently executing function.

[`arguments.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length)

The number of arguments passed to the function.

### [Getter and setter functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#getter_and_setter_functions)

You can define accessor properties on any standard built-in object or user-defined object that supports the addition of new properties. Within [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 and [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
, you can use special syntaxes to define the getter and setter of an accessor property.

[get](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)

Binds an object property to a function that will be called when that property is looked up.

[set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)

Binds an object property to a function to be called when there is an attempt to set that property.

Note that these syntaxes create an _object property_, not a _method_. The getter and setter functions themselves can only be accessed using reflective APIs such as [`Object.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor)
.

### [Block-level functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#block-level_functions)

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, functions inside blocks are scoped to that block. Prior to ES2015, block-level functions were forbidden in strict mode.

### [Block-level functions in non-strict code](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#block-level_functions_in_non-strict_code)

In a word: **Don't.**

In non-strict code, function declarations inside blocks behave strangely. For example:

The semantics of this in strict mode are well-specified — `zero` only ever exists within that scope of the `if` block. If `shouldDefineZero` is false, then `zero` should never be defined, since the block never executes. However, historically, this was left unspecified, so different browsers implemented it differently in non-strict mode. For more information, see the [`function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function#block-level_function_declaration)
 reference.

A safer way to define functions conditionally is to assign a function expression to a variable:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#examples)

-------------------------------------------------------------------------------------------------

### [Returning a formatted number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#returning_a_formatted_number)

The following function returns a string containing the formatted representation of a number padded with leading zeros.

The following statements call the `padZeros` function.

### [Determining whether a function exists](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#determining_whether_a_function_exists)

You can determine whether a function exists by using the [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 operator. In the following example, a test is performed to determine if the `window` object has a property called `noFunc` that is a function. If so, it is used; otherwise, some other action is taken.

Note that in the `if` test, a reference to `noFunc` is used — there are no parentheses `()` after the function name so the actual function is not called.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#see_also)

-------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
    
*   [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")