*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#mdn-search)
    

SyntaxError: property name \_\_proto\_\_ appears more than once in object literal
=================================================================================

The JavaScript exception "property name \_\_proto\_\_ appears more than once in object literal" occurs when an [object literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 contains multiple occurrences of the `__proto__` field, which is used to [set the prototype of this new object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#prototype_setter)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#message)

------------------------------------------------------------------------------------------------------------

SyntaxError: Duplicate \_\_proto\_\_ fields are not allowed in object literals (V8-based)
SyntaxError: property name \_\_proto\_\_ appears more than once in object literal (Firefox)
SyntaxError: Attempted to redefine \_\_proto\_\_ property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#error_type)

------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------

The `__proto__` key, unlike other property keys, is a special syntax in an object literal. It is used to set the prototype of the object being created and is not allowed to appear more than once in an object literal. Note that this restriction only applies to the `__proto__` prototype setter syntax: if it actually has the effect of creating a property called `__proto__`, then it can appear multiple times. See [prototype setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#prototype_setter)
 for the exact syntax restrictions.

Worth noting that the `__proto__` key in object literals is a special syntax and is not deprecated, unlike the [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)
 accessor property.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#examples)

--------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#invalid_cases)

js

    const obj = { __proto__: {}, __proto__: { a: 1 } };
    

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#valid_cases)

js

    // Only setting the prototype once
    const obj = { __proto__: { a: 1 } };
    
    // These syntaxes all create a property called "__proto__" and can coexist
    // They would overwrite each other and the last one is actually used
    const __proto__ = null;
    const obj2 = {
      ["__proto__"]: {},
      __proto__,
      __proto__() {},
      get __proto__() {
        return 1;
      },
    };
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
    
*   [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Duplicate_proto/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/duplicate_proto/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/duplicate_proto (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FDuplicate_proto&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fduplicate_proto%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FDuplicate_proto%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fduplicate_proto%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")