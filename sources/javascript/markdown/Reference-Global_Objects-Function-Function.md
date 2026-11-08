*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#mdn-search)
    

Function() constructor
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** The arguments passed to this constructor are dynamically parsed and executed as JavaScript. APIs like this are known as [injection sinks](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#concepts_and_usage)
, and are potentially a vector for [cross-site-scripting (XSS)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS)
 attacks.

You can mitigate this risk by always passing [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 objects instead of strings and [enforcing trusted types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
.

See [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#security_considerations)
 for more information.

The **`Function()`** constructor creates [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 objects. Calling the constructor directly can create functions dynamically, but suffers from security and similar (but far less significant) performance issues as [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
. However, unlike `eval` (which may have access to the local scope), the `Function` constructor creates functions which execute in the global scope only.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#try_it)

--------------------------------------------------------------------------------------------------------------------

    const sum = new Function("a", "b", "return a + b");
    
    console.log(sum(2, 6));
    // Expected output: 8
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#syntax)

--------------------------------------------------------------------------------------------------------------------

js

    new Function(functionBody)
    new Function(arg1, functionBody)
    new Function(arg1, arg2, functionBody)
    new Function(arg1, arg2, /* …, */ argN, functionBody)
    
    Function(functionBody)
    Function(arg1, functionBody)
    Function(arg1, arg2, functionBody)
    Function(arg1, arg2, /* …, */ argN, functionBody)
    

**Note:** `Function()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Both create a new `Function` instance.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#parameters)

[`arg1`, …, `argN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#arg1)

[`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 instances or strings specifying names to be used by the function as formal argument names. The value must correspond to a valid JavaScript parameter (any of plain [identifier](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
, [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
, or [destructured](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 parameter, optionally with a [default](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
), or a list of such strings separated with commas.

As the parameters are parsed in the same way as function expressions, whitespace and comments are accepted. For example: `"x", "theValue = 42", "[a, b] /* numbers */"` — or `"x, theValue = 42, [a, b] /* numbers */"`. (`"x, theValue = 42", "[a, b]"` is also correct, though very confusing to read.)

[`functionBody`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#functionbody)

A [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 or a string containing the JavaScript statements comprising the function definition.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Function parameter arguments can't be parsed as a valid parameter list, or the `functionBody` can't be parsed as valid JavaScript statements.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Any parameter is a string when [Trusted Types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)
 are [enforced by a CSP](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
 and no default policy is defined.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#description)

------------------------------------------------------------------------------------------------------------------------------

`Function` objects created with the `Function` constructor are parsed when the function is created. This is less efficient than creating a function with a [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 or [function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 and calling it within your code, because such functions are parsed with the rest of the code.

All arguments passed to the function, except the last, are treated as the names of the identifiers of the parameters in the function to be created, in the order in which they are passed. The function will be dynamically compiled as a function expression, with the source assembled in the following fashion:

js

    `function anonymous(${args.join(",")}
    ) {
    ${functionBody}
    }`;
    

This is observable by calling the function's [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/toString)
 method.

However, unlike normal [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
, the name `anonymous` is not added to the `functionBody`'s scope, since `functionBody` only has access the global scope. If `functionBody` is not in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 (the body itself needs to have the `"use strict"` directive since it doesn't inherit the strictness from the context), you may use [`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)
 to refer to the function itself. Alternatively, you can define the recursive part as an inner function:

js

    const recursiveFn = new Function(
      "count",
      `
    (function recursiveFn(count) {
      if (count < 0) {
        return;
      }
      console.log(count);
      recursiveFn(count - 1);
    })(count);
    `,
    );
    

Note that the two dynamic parts of the assembled source — the parameters list `args.join(",")` and `functionBody` — will first be parsed separately to ensure they are each syntactically valid. This prevents injection-like attempts.

js

    new Function("/*", "*/) {");
    // SyntaxError: Unexpected end of arg string
    // Doesn't become "function anonymous(/*) {*/) {}"
    

### [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#security_considerations)

The method can be used to execute arbitrary input passed to any parameter. If the input is a potentially unsafe string provided by a user, this is a possible vector for [Cross-site-scripting (XSS)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS)
 attacks. For example, the following example assumes the `untrustedCode` was provided by a user:

js

    const untrustedCode = "alert('Potentially evil code!');";
    const adder = new Function("a", "b", untrustedCode);
    

Websites with a [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 that specifies [`script-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src)
 or [`default-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/default-src)
 will prevent such code running by default. If you must allow the scripts to run via `Function()`, you can mitigate these issues by always assigning [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 objects instead of strings, and [enforcing trusted types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
 using the [`require-trusted-types-for`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/require-trusted-types-for)
 CSP directive. This ensures that the input is passed through a transformation function.

To allow `Function()` to run, you additionally need to specify the [`trusted-types-eval` keyword](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#trusted-types-eval)
 in your CSP `script-src` directive. The [`unsafe-eval`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#unsafe-eval)
 keyword also allows `Function()`, but is much less safe than `trusted-types-eval` because it would allow execution even on browsers that do not support trusted types.

For example, the required CSP for your site might look like this:

http

    Content-Security-Policy: require-trusted-types-for 'script'; script-src '<your_allowlist>' 'trusted-types-eval'
    

The behavior of the transformation function depends on the specific use case that requires a user-provided script. If possible, you should lock the allowed scripts to exactly the code that you trust to run. If that is not possible, you might allow or block the use of certain functions within the provided string.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#examples)

------------------------------------------------------------------------------------------------------------------------

Note that these examples omit the use of trusted types for brevity. For code showing the recommended approach, see [Using `TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#using_trustedscript)
 in `eval()`.

### [Specifying arguments with the Function constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#specifying_arguments_with_the_function_constructor)

The following code creates a `Function` object that takes two arguments.

js

    // Example can be run directly in your JavaScript console
    
    // Create a function that takes two arguments, and returns the sum of those arguments
    const adder = new Function("a", "b", "return a + b");
    
    // Call the function
    adder(2, 6);
    // 8
    

The arguments `a` and `b` are formal argument names that are used in the function body, `return a + b`.

### [Creating a function object from a function declaration or function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#creating_a_function_object_from_a_function_declaration_or_function_expression)

js

    // The function constructor can take in multiple statements separated by a semicolon. Function expressions require a return statement with the function's name
    
    // Observe that new Function is called. This is so we can call the function we created directly afterwards
    const sumOfArray = new Function(
      "const sumArray = (arr) => arr.reduce((previousValue, currentValue) => previousValue + currentValue); return sumArray",
    )();
    
    // call the function
    sumOfArray([1, 2, 3, 4]);
    // 10
    
    // If you don't call new Function at the point of creation, you can use the Function.call() method to call it
    const findLargestNumber = new Function(
      "function findLargestNumber (arr) { return Math.max(...arr) }; return findLargestNumber",
    );
    
    // call the function
    findLargestNumber.call({}).call({}, [2, 4, 1, 8, 5]);
    // 8
    
    // Function declarations do not require a return statement
    const sayHello = new Function(
      "return function (name) { return `Hello, ${name}` }",
    )();
    
    // call the function
    sayHello("world");
    // Hello, world
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-constructor](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-function-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Using the function constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#using_the_function_constructor)
     in `eval()`
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
    
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/function/function/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/function/function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2FFunction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Ffunction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2FFunction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Ffunction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06f8ebf948372dfb6c3c22d26d4f672c99cd4e0d%0A*+Document+last+modified%3A+2026-10-08T05%3A24%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")