*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#mdn-search)
    

Function.prototype.caller
=========================

Deprecated

Avoid using this feature in new projects. JavaScript strict mode prohibits accessing the `caller` and `arguments` properties of a `Function` object. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Note:** In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, accessing `caller` of a function throws an error — the API is removed with no replacement. This is to prevent code from being able to "walk the stack", which both poses security risks and severely limits the possibility of optimizations like inlining and tail-call optimization. For more explanation, you can read [the rationale for the deprecation of `arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee#description)
.

The **`caller`** accessor property of [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 instances returns the function that invoked this function. For [strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, arrow, async, and generator functions, accessing the `caller` property throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#description)

----------------------------------------------------------------------------------------------------------------------------

If the function `f` was invoked by the top-level code, the value of `f.caller` is [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
; otherwise it's the function that called `f`. If the function that called `f` is a strict mode function, the value of `f.caller` is also `null`.

Note that the only behavior specified by the ECMAScript specification is that `Function.prototype` has an initial `caller` accessor that unconditionally throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 for any `get` or `set` request (known as a "poison pill accessor"), and that implementations are not allowed to change this semantic for any function except non-strict plain functions, in which case it must not have the value of a strict mode function. The actual behavior of the `caller` property, if it's anything other than throwing an error, is implementation-defined. For example, Chrome defines it as an own data property, while Firefox and Safari extend the initial poison-pill `Function.prototype.caller` accessor to specially handle `this` values that are non-strict functions.

This property replaces the obsolete `arguments.caller` property of the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object.

The special property `__caller__`, which returned the activation object of the caller thus allowing you to reconstruct the stack, was removed for security reasons.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#examples)

----------------------------------------------------------------------------------------------------------------------

### [Checking the value of a function's caller property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#checking_the_value_of_a_functions_caller_property)

The following code checks the value a function's `caller` property.

### [Reconstructing the stack and recursion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#reconstructing_the_stack_and_recursion)

Note that in case of recursion, you can't reconstruct the call stack using this property. Consider:

At the moment `stop()` is called the call stack will be:

f(2) -> g(1) -> f(1) -> g(0) -> stop()

The following is true:

so if you tried to get the stack trace in the `stop()` function like this:

the loop would never stop.

### [Strict mode caller](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#strict_mode_caller)

If the caller is a strict mode function, the value of `caller` is `null`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#specifications)

----------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`Function.prototype.name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name)
    
*   [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/function/caller/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/function/caller (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fcaller&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fcaller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fcaller%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fcaller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")