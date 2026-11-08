*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#mdn-search)
    

arguments.callee
================

Deprecated

Avoid using this feature in new projects. JavaScript strict mode prohibits accessing `arguments.callee`. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** Accessing `arguments.callee` in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
. If a function must reference itself, either give the [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 a name or use a [function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
.

The **`arguments.callee`** data property contains the currently executing function that the arguments belong to.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#value)

------------------------------------------------------------------------------------------------------------

A reference to the currently executing function.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | yes |

**Note:** `callee` is a data property only in non-strict functions with simple parameters (in which case the `arguments` object is also [auto-syncing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments#assigning_to_indices)
). Otherwise, it is an accessor property whose getter and setter both throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#description)

------------------------------------------------------------------------------------------------------------------------

`callee` is a property of the `arguments` object. It can be used to refer to the currently executing function inside the function body of that function. This is useful when the name of the function is unknown, such as within a function expression with no name (also called "anonymous functions").

(The text below is largely adapted from [a Stack Overflow answer by olliej](https://stackoverflow.com/questions/103598/why-was-the-arguments-callee-caller-property-deprecated-in-javascript/235760 "External link (opens in new tab)")
)

Early versions of JavaScript did not allow named function expressions, and for this reason you could not make a recursive function expression.

For example, this syntax worked:

but:

did not. To get around this `arguments.callee` was added so you could do

However, the design of `arguments.callee` has multiple issues. The first problem is that the recursive call will get a different `this` value. For example:

In addition, references to `arguments.callee` make inlining and tail recursion impossible in the general case. (You can achieve it in select cases through tracing, etc., but even the best code is suboptimal due to checks that would not otherwise be necessary.)

ECMAScript 3 resolved these issues by allowing named function expressions. For example:

This has numerous benefits:

*   the function can be called like any other from inside your code
*   it does not create a variable in the outer scope ([except for IE 8 and below](https://kangax.github.io/nfe/#example_1_function_expression_identifier_leaks_into_an_enclosing_scope "External link (opens in new tab)")
    )
*   it has better performance than accessing the arguments object

Strict mode has banned other properties that leak stack information, like the [`caller`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller)
 property of functions. This is because looking at the call stack has one single major effect: it makes a large number of optimizations impossible, or much more difficult. For example, if you cannot guarantee that a function `f` will not call an unknown function, it is not possible to inline `f`.

If the JavaScript interpreter cannot guarantee that all the provided arguments are numbers at the point that the call is made, it needs to either insert checks for all the arguments before the inlined code, or it cannot inline the function. This means any call site that may have been trivially inlinable accumulates a large number of guards. Now in this particular case a smart interpreter should be able to rearrange the checks to be more optimal and not check any values that would not be used. However in many cases that's just not possible and therefore it becomes impossible to inline.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#examples)

------------------------------------------------------------------------------------------------------------------

### [Using arguments.callee in an anonymous recursive function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#using_arguments.callee_in_an_anonymous_recursive_function)

A recursive function must be able to refer to itself. Typically, a function refers to itself by its name. However, an anonymous function (which can be created by a [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 or the [`Function` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
) does not have a name. Therefore if there is no accessible variable referring to it, the only way the function can refer to itself is by `arguments.callee`.

The following example defines a function, which, in turn, defines and returns a factorial function. This example isn't very practical, and there are nearly no cases where the same result cannot be achieved with [named function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
.

### [Recursion of anonymous functions with a Y-combinator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#recursion_of_anonymous_functions_with_a_y-combinator)

Although function expressions can now be named, [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 always remain anonymous, which means they cannot reference themselves without being assigned to a variable first. Fortunately, in Lambda calculus there's a very good solution which allows a function to both be anonymous and self-referential. The technique is called a [Y-combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator "External link (opens in new tab)")
. Here we will not explain _how_ it works, only _that_ it works.

**Note:** This method allocates a new closure for every iteration, which may significantly increase memory usage. It's only here to demonstrate the possibility, but should be avoided in production. Use a temporary variable or a named function expression instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-arguments-exotic-objects](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-arguments-exotic-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
    
*   [`Function.prototype.caller`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/arguments/callee/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/arguments/callee (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments%2Fcallee&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%2Fcallee%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments%2Fcallee%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%2Fcallee%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")