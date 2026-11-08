*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#mdn-search)
    

Rest parameters
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **rest parameter** syntax allows a function to accept an indefinite number of arguments as an array, providing a way to represent [variadic functions](https://en.wikipedia.org/wiki/Variadic_function "External link (opens in new tab)")
 in JavaScript.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#syntax)

-------------------------------------------------------------------------------------------------------------

There are some additional syntax restrictions:

*   A function definition can only have one rest parameter.
*   The rest parameter must be the last parameter in the function definition.
*   [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas)
     are not allowed after the rest parameter.
*   The rest parameter cannot have a [default value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
    .

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#description)

-----------------------------------------------------------------------------------------------------------------------

A function definition's last parameter can be prefixed with `...` (three U+002E FULL STOP characters), which will cause all remaining (user supplied) parameters to be placed within an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 object.

The rest parameter may be [destructured](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
, which allows you to ignore certain parameter positions.

However, the following are all syntax errors:

The rest parameter is not counted towards the function's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
 property.

### [The difference between rest parameters and the arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#the_difference_between_rest_parameters_and_the_arguments_object)

There are four main differences between rest parameters and the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object:

*   The `arguments` object is **not a real array**, while rest parameters are [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
     instances, meaning methods like [`sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
    , [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
    , [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
     or [`pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
     can be applied on it directly.
*   The `arguments` object has the additional (deprecated) [`callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)
     property.
*   In a non-strict function with simple parameters, the `arguments` object [syncs its indices with the values of parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#assigning_to_indices)
    . The rest parameter array never updates its value when the named parameters are re-assigned.
*   The rest parameter bundles all the _extra_ parameters into a single array, but does not contain any named argument defined _before_ the `...restParam`. The `arguments` object contains all of the parameters — including the parameters in the `...restParam` array — bundled into one array-like object.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#using_rest_parameters)

In this example, the first argument is mapped to `a` and the second to `b`, so these named arguments are used as normal.

However, the third argument, `manyMoreArgs`, will be an array that contains the third, fourth, fifth, sixth, …, nth — as many arguments as the user specifies.

Below, even though there is just one value, the last argument still gets put into an array.

Below, the third argument isn't provided, but `manyMoreArgs` is still an array (albeit an empty one).

Below, only one argument is provided, so `b` gets the default value `undefined`, but `manyMoreArgs` is still an empty array.

### [Argument length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#argument_length)

Since `theArgs` is an array, a count of its elements is given by the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property. If the function's only parameter is a rest parameter, `restParams.length` will be equal to [`arguments.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length)
.

### [Using rest parameters in combination with ordinary parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#using_rest_parameters_in_combination_with_ordinary_parameters)

In the next example, a rest parameter is used to collect all parameters after the first parameter into an array. Each one of the parameter values collected into the array is then multiplied by the first parameter, and the array is returned:

### [From arguments to an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#from_arguments_to_an_array)

[`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 methods can be used on rest parameters, but not on the `arguments` object:

Rest parameters were introduced to reduce the boilerplate code that was commonly used for converting a set of arguments to an array.

Before rest parameters, `arguments` need to be converted to a normal array before calling array methods on them:

Now, you can easily gain access to a normal array using a rest parameter:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [Spread syntax (`...`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
    
*   [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
    
*   [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
    
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/rest_parameters/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/rest_parameters (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Frest_parameters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Frest_parameters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Frest_parameters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Frest_parameters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")