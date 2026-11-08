*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#mdn-search)
    

eval()
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** The argument passed to this function is dynamically parsed and executed as JavaScript. APIs like this are known as [injection sinks](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#concepts_and_usage)
, and are potentially a vector for [cross-site-scripting (XSS)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS)
 attacks.

You can mitigate this risk by always passing [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 objects instead of strings and [enforcing trusted types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
.

See [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#security_considerations)
 for more information.

The **`eval()`** function evaluates JavaScript code represented as a string and returns its completion value. The source is parsed as a script.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#syntax)

-------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#parameters)

[`script`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#script)

A [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 instance or string representing a JavaScript expression, statement, or sequence of statements. The expression can include variables and properties of existing objects. It will be parsed as a script, so [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
 declarations (which can only exist in modules) are not allowed.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#return_value)

The completion value of evaluating the given code. If the completion value is empty, [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 is returned. If `script` is not a [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 or string primitive, `eval()` returns the argument unchanged.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

The `script` parameter cannot be parsed as a script.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

`script` is a string when [Trusted Types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)
 are [enforced by a CSP](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
 and no default policy is defined.

The method also throws any exception that occurs during evaluation of the code.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#description)

-----------------------------------------------------------------------------------------------------------------

`eval()` is a function property of the global object.

The argument of the `eval()` function is a string. It will evaluate the source string as a script body, which means both statements and expressions are allowed. It returns the completion value of the code. For expressions, it's the value the expression evaluates to. Many statements and declarations have completion values as well, but the result may be surprising (for example, the completion value of an assignment is the assigned value, but the completion value of [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 is undefined), so it's recommended to not rely on statements' completion values.

In strict mode, declaring a variable named `eval` or re-assigning `eval` is a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

If the argument of `eval()` is not a [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 or string, `eval()` returns the argument unchanged. In the following example, passing a `String` object instead of a primitive causes `eval()` to return the `String` object rather than evaluating the string.

To work around the issue in a generic fashion, you can [coerce the argument to a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
 yourself before passing it to `eval()`.

### [Direct and indirect eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#direct_and_indirect_eval)

There are two modes of `eval()` calls: _direct_ eval and _indirect_ eval. Direct eval, as the name implies, refers to _directly_ calling the global `eval` function with `eval(...)`. Everything else, including invoking it via an aliased variable, via a member access or other expression, or through the optional chaining [`?.`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
 operator, is indirect.

Indirect eval can be seen as if the code is evaluated within a separate `<script>` tag. This means:

*   Indirect eval works in the global scope rather than the local scope, and the code being evaluated doesn't have access to local variables within the scope where it's being called.
    
*   Indirect `eval` does not inherit the strictness of the surrounding context, and is only in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
     if the source string itself has a `"use strict"` directive.
    
    On the other hand, direct eval inherits the strictness of the invoking context.
    
*   `var`\-declared variables and [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
     would go into the surrounding scope if the source string is not interpreted in strict mode — for indirect eval, they become global variables. If it's a direct eval in a strict mode context, or if the `eval` source string itself is in strict mode, then `var` and function declarations do not "leak" into the surrounding scope.
    
    [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
     and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
     declarations within the evaluated string are always scoped to that script.
    
*   Direct eval may have access to additional contextual expressions. For example, in a function's body, one can use [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
    :
    

### [Never use direct eval()!](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#never_use_direct_eval!)

Using direct `eval()` suffers from multiple problems:

*   `eval()` executes the code it's passed with the privileges of the caller. If you run `eval()` with a string that could be affected by a malicious party, you may end up running malicious code on the user's machine with the permissions of your webpage / extension. More importantly, allowing third-party code to access the scope in which `eval()` was invoked (if it's a direct eval) can lead to possible attacks that reads or changes local variables. See [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#security_considerations)
     for approaches that mitigate these risks.
*   `eval()` is slower than the alternatives, since it has to invoke the JavaScript interpreter, while many other constructs are optimized by modern JS engines.
*   Modern JavaScript interpreters convert JavaScript to machine code. This means that any concept of variable naming gets obliterated. Thus, any use of `eval()` will force the browser to do long expensive variable name lookups to figure out where the variable exists in the machine code and set its value. Additionally, new things can be introduced to that variable through `eval()`, such as changing the type of that variable, forcing the browser to re-evaluate all of the generated machine code to compensate.
*   Minifiers give up on any minification if the scope is transitively depended on by `eval()`, because otherwise `eval()` cannot read the correct variable at runtime.

There are many cases where the use of `eval()` or related methods can be optimized or avoided altogether.

#### Using indirect eval()

Consider this code:

Simply using indirect eval and forcing strict mode can make the code much better:

The two code snippets above may seem to work the same way, but they do not; the first one using direct eval suffers from multiple problems.

*   It is a great deal slower, due to more scope inspections. Notice `c: new Map()` in the evaluated string. In the indirect eval version, the object is being evaluated in the global scope, so it is safe for the interpreter to assume that `Map` refers to the global `Map()` constructor instead of a local variable called `Map`. However, in the code using direct eval, the interpreter cannot assume this. For example, in the following code, `Map` in the evaluated string doesn't refer to `window.Map()`.
    
    Thus, in the `eval()` version of the code, the browser is forced to make the expensive lookup call to check to see if there are any local variables called `Map()`.
    
*   If not using strict mode, `var` declarations within the `eval()` source becomes variables in the surrounding scope. This leads to hard-to-debug issues if the string is acquired from external input, especially if there's an existing variable with the same name.
    
*   Direct eval can read and mutate bindings in the surrounding scope, which may lead to external input corrupting local data.
    
*   When using direct `eval`, especially when the eval source cannot be proven to be in strict mode, the engine — and build tools — have to disable all optimizations related to inlining, because the `eval()` source can depend on any variable name in its surrounding scope.
    

However, using indirect `eval()` does not allow passing extra bindings other than existing global variables for the evaluated source to read. If you need to specify additional variables that the evaluated source should have access to, consider using the `Function()` constructor.

#### Using the Function() constructor

The [`Function()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 constructor is very similar to the indirect eval example above: it also evaluates the JavaScript source passed to it in the global scope without reading or mutating any local bindings, and therefore allows engines to do more optimizations than direct `eval()`.

The difference between `eval()` and `Function()` is that the source string passed to `Function()` is parsed as a function body, not as a script. There are a few nuances — for example, you can use `return` statements at the top level of a function body, but not in a script.

The `Function()` constructor is useful if you wish to create local bindings within your eval source, by passing the variables as parameter bindings.

Both `eval()` and `Function()` implicitly evaluate arbitrary code, and are forbidden in strict [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 settings. There are also additional safer (and faster!) alternatives to `eval()` or `Function()` for common use-cases.

#### Using bracket accessors

You should not use `eval()` to access properties dynamically. Consider the following example where the property of the object to be accessed is not known until the code is executed. This can be done with `eval()`:

However, `eval()` is not necessary here — in fact, it's more error-prone, because if `propName` is not a valid identifier, it leads to a syntax error. Moreover, if `getPropName` is not a function you control, this may lead to execution of arbitrary code. Instead, use the [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
, which are much faster and safer:

You can even use this method to access descendant properties. Using `eval()`, this would look like:

Avoiding `eval()` here could be done by splitting the property path and looping through the different properties:

Setting a property that way works similarly:

However, beware that using bracket accessors with unconstrained input is not safe either — it may lead to [object injection attacks](https://github.com/eslint-community/eslint-plugin-security/blob/main/docs/the-dangers-of-square-bracket-notation.md "External link (opens in new tab)")
.

#### Using callbacks

JavaScript has [first-class functions](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)
, which means you can pass functions as arguments to other APIs, store them in variables and objects' properties, and so on. Many DOM APIs are designed with this in mind, so you can (and should) write:

[Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
 are also helpful as a way to create parameterized functions without concatenating strings.

#### Using JSON

If the string you're calling `eval()` on contains data (for example, an array: `"[1, 2, 3]"`), as opposed to code, you should consider switching to [JSON](https://developer.mozilla.org/en-US/docs/Glossary/JSON)
, which allows the string to use a subset of JavaScript syntax to represent data.

Note that since JSON syntax is limited compared to JavaScript syntax, many valid JavaScript literals will not parse as JSON. For example, trailing commas are not allowed in JSON, and property names (keys) in object literals must be enclosed in quotes. Be sure to use a JSON serializer to generate strings that will be later parsed as JSON.

Passing carefully constrained data instead of arbitrary code is a good idea in general. For example, an extension designed to scrape contents of web-pages could have the scraping rules defined in [XPath](https://developer.mozilla.org/en-US/docs/Web/XML/XPath)
 instead of JavaScript code.

### [Security considerations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#security_considerations)

The method can be used to execute arbitrary input with the privileges of the caller. If the input is a potentially unsafe string provided by a user, this is a possible vector for [Cross-site-scripting (XSS)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS)
 attacks.

For example, the following code shows how `eval()` might execute `untrustedCode` provided by a user:

Websites with a [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 that specifies [`script-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src)
 or [`default-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/default-src)
 will prevent such code running by default. If you must allow the scripts to run via `eval()`, you can mitigate the risks by always assigning a [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 instance instead of a string, and [enforcing trusted types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#using_a_csp_to_enforce_trusted_types)
 using the [`require-trusted-types-for`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/require-trusted-types-for)
 CSP directive. This ensures that the input is passed through a transformation function.

To allow `eval()` to run, you additionally need to specify the [`trusted-types-eval` keyword](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#trusted-types-eval)
 in your CSP `script-src` directive. The [`unsafe-eval`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#unsafe-eval)
 keyword also allows `eval()`, but is much less safe than `trusted-types-eval` because it would allow execution even on browsers that do not support trusted types.

For example, the required CSP for your site might look like this:

The behavior of the transformation function implemented in your trusted types policy depends on the specific use case that requires a user-provided script. If possible, you should lock the allowed scripts to exactly the code that you trust to run. If that is not possible, you might allow or block the use of certain functions within the provided input.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#examples)

-----------------------------------------------------------------------------------------------------------

Note that the first example shows how to use the method with trusted types. The other examples omit this step for brevity.

### [Using TrustedScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#using_trustedscript)

To mitigate the risk of XSS, we should always assign `TrustedScript` instances to the `script` parameter. We also need to do this if we're enforcing trusted types for other reasons and we want to allow some script sources that have been permitted (by `CSP: script-src`).

Trusted types are not yet supported on all browsers, so first we define the [trusted types tinyfill](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API#trusted_types_tinyfill)
. This acts as a transparent replacement for the Trusted Types JavaScript API:

Next we create a [`TrustedTypePolicy`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedTypePolicy)
 that defines a [`createScript()`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedTypePolicy/createScript "createScript()")
 method for transforming input strings into [`TrustedScript`](https://developer.mozilla.org/en-US/docs/Web/API/TrustedScript)
 instances.

For the purpose of this example, we'll assume that we have a function `transformedScript()` that defines our transformation/filtering logic.

Then we use the `policy` object to create a `TrustedScript` object from a potentially unsafe input string:

The `TrustedScript` object can now be passed to `eval()`:

### [Using eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#using_eval)

In the following code, both of the statements containing `eval()` return 42. The first evaluates the string `"x + y + 1"`; the second evaluates the string `"42"`.

### [eval() returns the completion value of statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#eval_returns_the_completion_value_of_statements)

`eval()` returns the completion value of statements. For `if`, it would be the last expression or statement evaluated.

The following example uses `eval()` to evaluate the string `str`. This string consists of JavaScript statements that assign `z` a value of 42 if `x` is five, and assign 0 to `z` otherwise. When the second statement is executed, `eval()` will cause these statements to be performed, and it will also evaluate the set of statements and return the value that is assigned to `z`, because the completion value of an assignment is the assigned value.

If you assign multiple values then the last value is returned.

### [eval() as a string defining function requires "(" and ")" as prefix and suffix](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#eval_as_a_string_defining_function_requires_and_as_prefix_and_suffix)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-eval-x](https://tc39.es/ecma262/multipage/global-object.html#sec-eval-x) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
    
*   [WebExtensions: Using eval in content scripts](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts#using_eval_in_content_scripts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/eval/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/eval (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2Feval&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Feval%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2Feval%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Feval%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06f8ebf948372dfb6c3c22d26d4f672c99cd4e0d%0A*+Document+last+modified%3A+2026-10-08T05%3A24%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")