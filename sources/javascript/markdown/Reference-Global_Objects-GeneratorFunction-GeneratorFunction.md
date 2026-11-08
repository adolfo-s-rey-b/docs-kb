*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#mdn-search)
    

GeneratorFunction() constructor
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** The arguments passed to this constructor are dynamically parsed and executed as JavaScript. APIs like this are known as [injection sinks](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#concepts_and_usage)
, and are potentially a vector for [cross-site-scripting (XSS)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS)
 attacks.

You can mitigate this risk by always passing [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 objects instead of strings and [enforcing trusted types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
.

See [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#security_considerations)
 in the `Function()` constructor reference for more information.

The **`GeneratorFunction()`** constructor creates [`GeneratorFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction)
 objects.

Note that `GeneratorFunction` is _not_ a global object. It can be obtained with the following code:

The `GeneratorFunction()` constructor is not intended to be used directly, and all caveats mentioned in the [`Function()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
 description apply to `GeneratorFunction()`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#syntax)

--------------------------------------------------------------------------------------------------------------------------------------

**Note:** `GeneratorFunction()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Both create a new `GeneratorFunction` instance.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#parameters)

See [`Function()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#examples)

------------------------------------------------------------------------------------------------------------------------------------------

Note that these examples omit the use of trusted types for brevity. For code showing the recommended approach, see [Using `TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#using_trustedscript)
 in `eval()`.

### [Creating and using a GeneratorFunction() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#creating_and_using_a_generatorfunction_constructor)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#specifications)

------------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-generatorfunction-constructor](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-generatorfunction-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction#see_also)

------------------------------------------------------------------------------------------------------------------------------------------

*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [`function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
    
*   [`Function()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
    
*   [Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction/GeneratorFunction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/generatorfunction/generatorfunction/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/generatorfunction/generatorfunction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FGeneratorFunction%2FGeneratorFunction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fgeneratorfunction%2Fgeneratorfunction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FGeneratorFunction%2FGeneratorFunction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fgeneratorfunction%2Fgeneratorfunction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffefa80c1e817377a0bbaf6a636ce6b8797f38fbb%0A*+Document+last+modified%3A+2026-01-21T19%3A07%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")