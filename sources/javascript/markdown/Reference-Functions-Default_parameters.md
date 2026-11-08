*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#mdn-search)
    

Default parameters
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Default function parameters** allow named parameters to be initialized with default values if no value or `undefined` is passed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#try_it)

----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#syntax)

----------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#description)

--------------------------------------------------------------------------------------------------------------------------

In JavaScript, function parameters default to [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. However, it's often useful to set a different default value. This is where default parameters can help.

In the following example, if no value is provided for `b` when `multiply` is called, `b`'s value would be `undefined` when evaluating `a * b` and `multiply` would return `NaN`.

In the past, the general strategy for setting defaults was to test parameter values in the function body and assign a value if they are `undefined`. In the following example, `b` is set to `1` if `multiply` is called with only one argument:

With default parameters, checks in the function body are no longer necessary. Now, you can assign `1` as the default value for `b` in the function head:

Parameters are still set left-to-right, overwriting default parameters even if there are later parameters without defaults.

**Note:** The first default parameter and all parameters after it will not contribute to the function's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
.

The default parameter initializers live in their own scope, which is a parent of the scope created for the function body.

This means that earlier parameters can be referred to in the initializers of later parameters. However, functions and variables declared in the function body cannot be referred to from default value parameter initializers; attempting to do so throws a run-time [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
. This also includes [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
\-declared variables in the function body.

For example, the following function will throw a `ReferenceError` when invoked, because the default parameter value does not have access to the child scope of the function body:

This function will print the value of the _parameter_ `a`, because the variable `var a` is hoisted only to the top of the scope created for the function body, not the parent scope created for the parameter list, so its value is not visible to `b`.

The default parameter allows any expression, but you cannot use [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 or [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 that would pause the evaluation of the default expression. The parameter must be initialized _synchronously_.

**Note:** Because the default parameter is evaluated when the function is called, not when the function is defined, the validity of the `await` and `yield` operators depends on the function itself, not its surrounding function. For example, if the current function is not `async`, `await` will be parsed as an identifier and follow normal [identifier syntax rules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
, even when this function is nested in an `async` function.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#examples)

--------------------------------------------------------------------------------------------------------------------

### [Passing undefined vs. other falsy values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#passing_undefined_vs._other_falsy_values)

In the second call in this example, even if the first argument is set explicitly to `undefined` (though not `null` or other [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 values), the value of the `num` argument is still the default.

### [Evaluated at call time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#evaluated_at_call_time)

The default argument is evaluated at _call time_. Unlike with Python (for example), a new object is created each time the function is called.

This even applies to functions and variables:

### [Earlier parameters are available to later default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#earlier_parameters_are_available_to_later_default_parameters)

Parameters defined earlier (to the left) are available to later default parameters:

This functionality can be approximated like this, which demonstrates how many edge cases are handled:

### [Destructured parameter with default value assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#destructured_parameter_with_default_value_assignment)

You can use default value assignment with the [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 syntax.

A common way of doing that is to set an empty object/array as the default value for the destructured parameter; for example: `[x = 1, y = 2] = []`. This makes it possible to pass nothing to the function and still have those values prefilled:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
    
*   [Nullish coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/default_parameters/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/default_parameters (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2FDefault_parameters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fdefault_parameters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2FDefault_parameters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fdefault_parameters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")