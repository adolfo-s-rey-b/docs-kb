*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#mdn-search)
    

Functions
=========

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
    

Functions are one of the fundamental building blocks in JavaScript. A function in JavaScript is similar to a procedure—a set of statements that performs a task or calculates a value, but for a procedure to qualify as a function, it should take some input and return an output where there is some obvious relationship between the input and the output. To use a function, you must define it somewhere in the scope from which you wish to call it.

See also the [exhaustive reference chapter about JavaScript functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 to get to know the details.

[Defining functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#defining_functions)

-----------------------------------------------------------------------------------------------------------------

### [Function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_declarations)

A **function definition** (also called a **function declaration**, or **function statement**) consists of the [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 keyword, followed by:

*   The name of the function.
*   A list of parameters to the function, enclosed in parentheses and separated by commas.
*   The JavaScript statements that define the function, enclosed in curly braces, `{ /* … */ }`.

For example, the following code defines a function named `square`:

The function `square` takes one parameter, called `number`. The function consists of one statement that says to return the parameter of the function (that is, `number`) multiplied by itself. The [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement specifies the value returned by the function, which is `number * number`.

Parameters are essentially passed to functions **by value** — so if the code within the body of a function assigns a completely new value to a parameter that was passed to the function, **the change is not reflected globally or in the code which called that function**.

When you pass an object as a parameter, if the function changes the object's properties, that change is visible outside the function, as shown in the following example:

When you pass an array as a parameter, if the function changes any of the array's values, that change is visible outside the function, as shown in the following example:

Function declarations and expressions can be nested, which forms a _scope chain_. For example:

See [function scopes and closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_scopes_and_closures)
 for more information.

### [Function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_expressions)

While the function declaration above is syntactically a statement, functions can also be created by a [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
.

Such a function can be **anonymous**; it does not have to have a name. For example, the function `square` could have been defined as:

However, a name _can_ be provided with a function expression. Providing a name allows the function to refer to itself, and also makes it easier to identify the function in a debugger's stack traces:

Function expressions are convenient when passing a function as an argument to another function. The following example defines a `map` function that should receive a function as first argument and an array as second argument. Then, it is called with a function defined by a function expression:

In JavaScript, a function can be defined based on a condition. For example, the following function definition defines `myFunc` only if `num` equals `0`:

In addition to defining functions as described here, you can also use the [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 constructor to create functions from a string at runtime, much like [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
.

A **method** is a function that is a property of an object. Read more about objects and methods in [Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
.

[Calling functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#calling_functions)

---------------------------------------------------------------------------------------------------------------

_Defining_ a function does not _execute_ it. Defining it names the function and specifies what to do when the function is called.

**Calling** the function actually performs the specified actions with the indicated parameters. For example, if you define the function `square`, you could call it as follows:

The preceding statement calls the function with an argument of `5`. The function executes its statements and returns the value `25`.

Functions must be _in scope_ when they are called, but the function declaration can be [hoisted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_hoisting)
 (appear below the call in the code). The scope of a function declaration is the function in which it is declared (or the entire program, if it is declared at the top level).

The arguments of a function are not limited to strings and numbers. You can pass whole objects to a function. The `showProps()` function (defined in [Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#objects_and_properties)
) is an example of a function that takes an object as an argument.

A function can call itself. For example, here is a function that computes factorials recursively:

You could then compute the factorials of `1` through `5` as follows:

There are other ways to call functions. There are often cases where a function needs to be called dynamically, or the number of arguments to a function vary, or in which the context of the function call needs to be set to a specific object determined at runtime.

It turns out that _functions are themselves objects_ — and in turn, these objects have methods. (See the [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 object.) The [`call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 and [`apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 methods can be used to achieve this goal.

### [Function hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_hoisting)

Consider the example below:

This code runs without any error, despite the `square()` function being called before it's declared. This is because the JavaScript interpreter hoists the entire function declaration to the top of the current scope, so the code above is equivalent to:

Function hoisting only works with function _declarations_ — not with function _expressions_. The following code will not work:

### [Recursion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#recursion)

A function can refer to and call itself. It can be referred to either by the function expression or declaration's name, or via any in-scope variable that refers to the function object. For example, consider the following function definition:

Within the function body, you can refer to the function itself either as `bar` or `foo`, and call itself using `bar()` or `foo()`.

A function that calls itself is called a _recursive function_. In some ways, recursion is analogous to a loop. Both execute the same code multiple times, and both require a condition (to avoid an infinite loop, or rather, infinite recursion in this case).

For example, consider the following loop:

It can be converted into a recursive function declaration, followed by a call to that function:

However, some algorithms cannot be simple iterative loops. For example, getting all the nodes of a tree structure (such as the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
) is easier via recursion:

Compared to the function `loop`, each recursive call itself makes many recursive calls here.

It is possible to convert any recursive algorithm to a non-recursive one, but the logic is often much more complex, and doing so requires the use of a stack.

In fact, recursion itself uses a stack: the function stack. The stack-like behavior can be seen in the following example:

### [Immediately Invoked Function Expressions (IIFE)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#immediately_invoked_function_expressions_iife)

An [Immediately Invoked Function Expression (IIFE)](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 is a code pattern that directly calls a function defined as an expression. It looks like this:

Instead of saving the function in a variable, the function is immediately invoked. This is almost equivalent to just writing the function body, but there are a few unique benefits:

*   It creates an extra [scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_scopes_and_closures)
     of variables, which helps to confine variables to the place where they are useful.
*   It is now an _expression_ instead of a sequence of _statements_. This allows you to write complex computation logic when initializing variables.

For more information, see the [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 glossary entry.

[Function scopes and closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_scopes_and_closures)

-------------------------------------------------------------------------------------------------------------------------------------

Functions form a [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
 for variables—this means variables defined inside a function cannot be accessed from anywhere outside the function. The function scope inherits from all the upper scopes. For example, a function defined in the global scope can access all variables defined in the global scope. A function defined inside another function can also access all variables defined in its parent function, and any other variables to which the parent function has access. On the other hand, the parent function (and any other parent scope) does _not_ have access to the variables and functions defined inside the inner function. This provides a sort of encapsulation for the variables in the inner function.

### [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#closures)

We also refer to the function body as a _closure_. A closure is any piece of source code (most commonly, a function) that refers to some variables, and the closure "remembers" these variables even when the scope in which these variables were declared has exited.

Closures are usually illustrated with nested functions to show that they remember variables beyond the lifetime of its parent scope; but in fact, nested functions are unnecessary. Technically speaking, all functions in JavaScript form closures—some just don't capture anything, and closures don't even have to be functions. The key ingredients for a _useful_ closure are the following:

*   A parent scope that defines some variables or functions. It should have a clear lifetime, which means it should finish execution at some point. Any scope that's not the global scope satisfies this requirement; this includes blocks, functions, modules, and more.
*   An inner scope defined within the parent scope, which refers to some variables or functions defined in the parent scope.
*   The inner scope manages to survive beyond the lifetime of the parent scope. For example, it is saved to a variable that's defined outside the parent scope, or it's returned from the parent scope (if the parent scope is a function).
*   Then, when you call the function outside of the parent scope, you can still access the variables or functions that were defined in the parent scope, even though the parent scope has finished execution.

The following is a typical example of a closure:

It can be much more complex than the code above. An object containing methods for manipulating the inner variables of the outer function can be returned.

In the code above, the `name` variable of the outer function is accessible to the inner functions, and there is no other way to access the inner variables except through the inner functions. The inner variables of the inner functions act as safe stores for the outer arguments and variables. They hold "persistent" and "encapsulated" data for the inner functions to work with. The functions do not even have to be assigned to a variable, or have a name.

In the code above, we use the [IIFE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#immediately_invoked_function_expressions_iife)
 pattern. Within this IIFE scope, two values exist: a variable `apiCode` and an unnamed function that gets returned and gets assigned to the variable `getCode`. `apiCode` is in the scope of the returned unnamed function but not in the scope of any other part of the program, so there is no way for reading the value of `apiCode` apart from via the `getCode` function.

### [Multiply-nested functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#multiply-nested_functions)

Functions can be multiply-nested. For example:

*   A function (`A`) contains a function (`B`), which itself contains a function (`C`).
*   Both functions `B` and `C` form closures here. So, `B` can access `A`, and `C` can access `B`.
*   In addition, since `C` can access `B` which can access `A`, `C` can also access `A`.

Thus, the closures can contain multiple scopes; they recursively contain the scope of the functions containing it. This is called _scope chaining_. Consider the following example:

In this example, `C` accesses `B`'s `y` and `A`'s `x`. This can be done because:

1.  `B` forms a closure including `A` (i.e., `B` can access `A`'s arguments and variables).
2.  `C` forms a closure including `B`.
3.  Because `C`'s closure includes `B` and `B`'s closure includes `A`, then `C`'s closure also includes `A`. This means `C` can access _both_ `B` _and_ `A`'s arguments and variables. In other words, `C` _chains_ the scopes of `B` and `A`, _in that order_.

The reverse, however, is not true. `A` cannot access `C`, because `A` cannot access any argument or variable of `B`, which `C` is a variable of. Thus, `C` remains private to only `B`.

### [Name conflicts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#name_conflicts)

When two arguments or variables in the scopes of a closure have the same name, there is a _name conflict_. More nested scopes take precedence. So, the innermost scope takes the highest precedence, while the outermost scope takes the lowest. This is the scope chain. The first on the chain is the innermost scope, and the last is the outermost scope. Consider the following:

The name conflict happens at the statement `return x * 2` and is between `inside`'s parameter `x` and `outside`'s variable `x`. The scope chain here is `inside` => `outside` => global object. Therefore, `inside`'s `x` takes precedences over `outside`'s `x`, and `20` (`inside`'s `x`) is returned instead of `10` (`outside`'s `x`).

[Using the arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#using_the_arguments_object)

---------------------------------------------------------------------------------------------------------------------------------

The arguments of a function are maintained in an array-like object. Within a function, you can address the arguments passed to it as follows:

where `i` is the ordinal number of the argument, starting at `0`. So, the first argument passed to a function would be `arguments[0]`. The total number of arguments is indicated by `arguments.length`.

Using the `arguments` object, you can call a function with more arguments than it is formally declared to accept. This is often useful if you don't know in advance how many arguments will be passed to the function. You can use `arguments.length` to determine the number of arguments actually passed to the function, and then access each argument using the `arguments` object.

For example, consider a function that concatenates several strings. The only formal argument for the function is a string that specifies the characters that separate the items to concatenate. The function is defined as follows:

You can pass any number of arguments to this function, and it concatenates each argument into a string "list":

**Note:** The `arguments` variable is "array-like", but not an array. It is array-like in that it has a numbered index and a `length` property. However, it does _not_ possess all of the array-manipulation methods.

See the [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 object in the JavaScript reference for more information.

[Function parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_parameters)

-------------------------------------------------------------------------------------------------------------------

There are two special kinds of parameter syntax: _default parameters_ and _rest parameters_.

### [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#default_parameters)

In JavaScript, parameters of functions default to `undefined`. However, in some situations it might be useful to set a different default value. This is exactly what default parameters do.

In the past, the general strategy for setting defaults was to test parameter values in the body of the function and assign a value if they are `undefined`.

In the following example, if no value is provided for `b`, its value would be `undefined` when evaluating `a*b`, and a call to `multiply` would normally have returned `NaN`. However, this is prevented by the second line in this example:

With _default parameters_, a manual check in the function body is no longer necessary. You can put `1` as the default value for `b` in the function head:

For more details, see [default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
 in the reference.

### [Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#rest_parameters)

The [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
 syntax allows us to represent an indefinite number of arguments as an array.

In the following example, the function `multiply` uses _rest parameters_ to collect arguments from the second one to the end. The function then multiplies these by the first argument.

[Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#arrow_functions)

-----------------------------------------------------------------------------------------------------------

An [arrow function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 (also called a _fat arrow_ to distinguish from a hypothetical `->` syntax in future JavaScript) has a shorter syntax compared to function expressions and does not have its own [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
, [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
, or [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
. Arrow functions are always anonymous.

Two factors influenced the introduction of arrow functions: _shorter functions_ and _non-binding_ of `this`.

### [Shorter functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#shorter_functions)

In some functional patterns, shorter functions are welcome. Compare:

### [No separate this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#no_separate_this)

Until arrow functions, every new function defined its own [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 value (a new object in the case of a constructor, undefined in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 function calls, the base object if the function is called as an "object method", etc.). This proved to be less than ideal with an object-oriented style of programming.

In ECMAScript 3/5, this issue was fixed by assigning the value in `this` to a variable that could be closed over.

Alternatively, a [bound function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 could be created so that the proper `this` value would be passed to the `growUp()` function.

An arrow function does not have its own `this`; the `this` value of the enclosing execution context is used. Thus, in the following code, the `this` within the function that is passed to `setInterval` has the same value as `this` in the enclosing function:

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/functions/index.md?plain=1 "Folder: en-us/web/javascript/guide/functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FFunctions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Ffunctions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FFunctions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Ffunctions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")