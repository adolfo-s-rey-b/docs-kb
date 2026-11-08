*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#mdn-search)
    

Assignment (=)
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **assignment (`=`)** operator is used to assign a value to a variable or property. The assignment expression itself has a value, which is the assigned value. This allows multiple assignments to be chained in order to assign a single value to multiple variables.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#try_it)

--------------------------------------------------------------------------------------------------------

    let x = 2;
    const y = 3;
    
    console.log(x);
    // Expected output: 2
    
    console.log((x = y + 1)); // 3 + 1
    // Expected output: 4
    
    console.log((x = x * y)); // 4 * 3
    // Expected output: 12
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#syntax)

--------------------------------------------------------------------------------------------------------

js

    x = y
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#parameters)

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#x)

A valid assignment target, including an [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 or a [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
. It can also be a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[`y`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#y)

An expression specifying the value to be assigned to `x`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#return_value)

The value of `y`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#exceptions)

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

Thrown in strict mode if assigning to an identifier that is not declared in the scope.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in strict mode if assigning to a [property that is not modifiable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#failing_to_assign_to_object_properties)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#description)

------------------------------------------------------------------------------------------------------------------

The assignment operator is completely different from the equals (`=`) sign used as syntactic separators in other locations, which include:

*   Initializers of [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    , [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    , and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
     declarations
*   Default values of [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#default_value)
    
*   [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
    
*   Initializers of [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
    

All these places accept an assignment expression on the right-hand side of the `=`, so if you have multiple equals signs chained together:

js

    const x = y = 5;
    

This is equivalent to:

js

    const x = (y = 5);
    

Which means `y` must be a pre-existing variable, and `x` is a newly declared `const` variable. `y` is assigned the value `5`, and `x` is initialized with the value of the `y = 5` expression, which is also `5`. If `y` is not a pre-existing variable, a global variable `y` is implicitly created in [non-strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, or a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
 is thrown in strict mode. To declare two variables within the same declaration, use:

js

    const x = 5,
      y = 5;
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#examples)

------------------------------------------------------------------------------------------------------------

### [Basic assignment and chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#basic_assignment_and_chaining)

js

    let x = 5;
    let y = 10;
    let z = 25;
    
    x = y; // x is 10
    x = y = z; // x, y and z are all 25
    

### [Value of assignment expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#value_of_assignment_expressions)

The assignment expression itself evaluates to the value of the right-hand side, so you can log the value and assign to a variable at the same time.

js

    let x;
    console.log(x); // undefined
    console.log(x = 2); // 2
    console.log(x); // 2
    

### [Unqualified identifier assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#unqualified_identifier_assignment)

The global object sits at the top of the scope chain. When attempting to resolve a name to a value, the scope chain is searched. This means that properties on the global object are conveniently visible from every scope, without having to qualify the names with `globalThis.` or `window.` or `global.`.

Because the global object has a `String` property (`Object.hasOwn(globalThis, "String")`), you can use the following code:

js

    function foo() {
      String("s"); // The function `String` is globally available
    }
    

So the global object will ultimately be searched for unqualified identifiers. You don't have to type `globalThis.String`; you can just type the unqualified `String`. To make this feature more conceptually consistent, assignment to unqualified identifiers will assume you want to create a property with that name on the global object (with `globalThis.` omitted), if there is no variable of the same name declared in the scope chain.

js

    foo = "f"; // In non-strict mode, assumes you want to create a property named `foo` on the global object
    Object.hasOwn(globalThis, "foo"); // true
    

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#assigning_to_undeclared_variables)
, assignment to an unqualified identifier in strict mode will result in a `ReferenceError`, to avoid the accidental creation of properties on the global object.

Note that the implication of the above is that, contrary to popular misinformation, JavaScript does not have implicit or undeclared variables. It just conflates the global object with the global scope and allows omitting the global object qualifier during property creation.

### [Assignment with destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#assignment_with_destructuring)

The left-hand side can also be an assignment pattern. This allows assigning to multiple variables at once.

js

    const result = /(a+)(b+)(c+)/.exec("aaabcc");
    let a = "",
      b = "",
      c = "";
    [, a, b, c] = result;
    console.log(a, b, c); // "aaa" "b" "cc"
    

For more information, see [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-assignment-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-assignment-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment#see_also)

------------------------------------------------------------------------------------------------------------

*   [Assignment operators in the JS guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#assignment_operators)
    
*   [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/assignment/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/assignment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FAssignment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fassignment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FAssignment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fassignment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")