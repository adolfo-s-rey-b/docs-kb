*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#mdn-search)
    

TypeError: "x" is (not) "y"
===========================

The JavaScript exception "_x_ is (not) _y_" occurs when there was an unexpected type. Oftentimes, unexpected [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 values.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#message)

------------------------------------------------------------------------------------------------------------

TypeError: Cannot read properties of undefined (reading 'x') (V8-based)
TypeError: "x" is undefined (Firefox)
TypeError: "undefined" is not an object (Firefox)
TypeError: undefined is not an object (evaluating 'obj.x') (Safari)

TypeError: "x" is not a symbol (V8-based & Firefox)
TypeError: Symbol.keyFor requires that the first argument be a symbol (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#error_type)

------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------

There was an unexpected type. This occurs oftentimes with [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 values.

Also, certain methods, such as [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
 or [`Symbol.keyFor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/keyFor)
, require a specific type, that must be provided.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#examples)

--------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#invalid_cases)

You cannot invoke a method on an `undefined` or `null` variable.

Certain methods might require a specific type.

### [Fixing the issue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#fixing_the_issue)

To fix null pointer to `undefined` or `null` values, you can test if the value is `undefined` or `null` first.

Or, if you are confident that `foo` will not be another [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 value like `""` or `0`, or if filtering those cases out is not an issue, you can simply test for its truthiness.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/unexpected_type/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/unexpected_type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnexpected_type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funexpected_type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnexpected_type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funexpected_type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")