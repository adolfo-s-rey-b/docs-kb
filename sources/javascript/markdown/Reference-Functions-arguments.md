*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#mdn-search)
    

The arguments object
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`arguments`** is an array-like object accessible inside [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
 that contains the values of the arguments passed to that function.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#try_it)

-------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#description)

-----------------------------------------------------------------------------------------------------------------

**Note:** In modern code, [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
 should be preferred.

The `arguments` object is a local variable available within all non-[arrow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 functions. You can refer to a function's arguments inside that function by using its `arguments` object. It has entries for each argument the function was called with, with the first entry's index at `0`.

For example, if a function is passed 3 arguments, you can access them as follows:

The `arguments` object is useful for functions called with more arguments than they are formally declared to accept, called [_variadic functions_](https://en.wikipedia.org/wiki/Variadic_function "External link (opens in new tab)")
, such as [`Math.min()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min)
. This example function accepts any number of string arguments and returns the longest one:

You can use [`arguments.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length)
 to count how many arguments the function was called with. If you instead want to count how many parameters a function is declared to accept, inspect that function's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
 property.

### [Assigning to indices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#assigning_to_indices)

Each argument index can also be set or reassigned:

Non-strict functions that only have simple parameters (that is, no rest, default, or destructured parameters) will sync the new value of parameters with the `arguments` object, and vice versa:

Non-strict functions that _are_ passed [rest](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
, [default](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
, or [destructured](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 parameters will not sync new values assigned to parameters in the function body with the `arguments` object. Instead, the `arguments` object in non-strict functions with complex parameters will always reflect the values passed to the function when the function was called.

This is the same behavior exhibited by all [strict-mode functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#making_eval_and_arguments_simpler)
, regardless of the type of parameters they are passed. That is, assigning new values to parameters in the body of the function never affects the `arguments` object, nor will assigning new values to the `arguments` indices affect the value of parameters, even when the function only has simple parameters.

**Note:** You cannot write a `"use strict";` directive in the body of a function definition that accepts rest, default, or destructured parameters. Doing so will throw [a syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Strict_non_simple_params)
.

### [arguments is an array-like object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#arguments_is_an_array-like_object)

`arguments` is an array-like object, which means that `arguments` has a [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length)
 property and properties indexed from zero, but it doesn't have [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
's built-in methods like [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 or [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
. However, it can be converted to a real `Array`, using one of [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
, or [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
.

For common use cases, using it as an array-like object is sufficient, since it both [is iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/Symbol.iterator)
 and has `length` and number indices. For example, [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 accepts array-like objects.

[Properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#properties)

---------------------------------------------------------------------------------------------------------------

[`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)

Reference to the currently executing function that the arguments belong to. Forbidden in strict mode.

[`arguments.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length)

The number of arguments that were passed to the function.

[`arguments[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/Symbol.iterator)

Returns a new [array iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.iterator)
 object that contains the values for each index in `arguments`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#examples)

-----------------------------------------------------------------------------------------------------------

### [Defining a function that concatenates several strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#defining_a_function_that_concatenates_several_strings)

This example defines a function that concatenates several strings. The function's only formal argument is a string containing the characters that separate the items to concatenate.

You can pass as many arguments as you like to this function. It returns a string list using each argument in the list:

### [Defining a function that creates HTML lists](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#defining_a_function_that_creates_html_lists)

This example defines a function that creates a string containing HTML for a list. The only formal argument for the function is a string that is `"u"` if the list is to be [unordered (bulleted)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
, or `"o"` if the list is to be [ordered (numbered)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
. The function is defined as follows:

You can pass any number of arguments to this function, and it adds each argument as a list item to a list of the type indicated. For example:

### [Using typeof with arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#using_typeof_with_arguments)

The [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 operator returns `'object'` when used with `arguments`:

The type of individual arguments can be determined by indexing `arguments`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-arguments-exotic-objects](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-arguments-exotic-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/arguments/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/arguments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")