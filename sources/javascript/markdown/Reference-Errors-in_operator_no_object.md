*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#mdn-search)
    

TypeError: cannot use 'in' operator to search for 'x' in 'y'
============================================================

The JavaScript exception "right-hand side of 'in' should be an object" occurs when the [`in` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 was used to search in strings, or in numbers, or other primitive types. It can only be used to check if a property is in an object.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#message)

------------------------------------------------------------------------------------------------------------------

TypeError: Cannot use 'in' operator to search for 'x' in 'y' (V8-based & Firefox)
TypeError: right-hand side of 'in' should be an object, got null (Firefox)
TypeError: "y" is not an Object. (evaluating '"x" in "y"') (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#error_type)

------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------------

The [`in` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 can only be used to check if a property is in an object. You can't search in strings, or in numbers, or other primitive types.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#examples)

--------------------------------------------------------------------------------------------------------------------

### [Searching in strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#searching_in_strings)

Unlike in other programming languages (e.g., Python), you can't search in strings using the [`in` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
.

js

    "Hello" in "Hello World";
    // TypeError: cannot use 'in' operator to search for 'Hello' in 'Hello World'
    

Instead you will need to use [`String.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)
, for example.

js

    "Hello World".includes("Hello");
    // true
    

### [The operand can't be null or undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#the_operand_cant_be_null_or_undefined)

Make sure the object you are inspecting isn't actually [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
.

js

    const foo = null;
    "bar" in foo;
    // TypeError: cannot use 'in' operator to search for 'bar' in 'foo' (Chrome)
    // TypeError: right-hand side of 'in' should be an object, got null (Firefox)
    

The `in` operator always expects an object.

js

    const foo = { baz: "bar" };
    "bar" in foo; // false
    
    "PI" in Math; // true
    "pi" in Math; // false
    

### [Searching in arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#searching_in_arrays)

Be careful when using the `in` operator to search in [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 objects. The `in` operator checks the index number, not the value at that index.

js

    const trees = ["redwood", "bay", "cedar", "oak", "maple"];
    3 in trees; // true
    "oak" in trees; // false
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/in_operator_no_object/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/in_operator_no_object/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/in_operator_no_object (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2Fin_operator_no_object&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fin_operator_no_object%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2Fin_operator_no_object%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fin_operator_no_object%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")