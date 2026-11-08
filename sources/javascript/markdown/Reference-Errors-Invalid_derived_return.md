*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#mdn-search)
    

TypeError: derived class constructor returned invalid value x
=============================================================

The JavaScript exception "derived class constructor returned invalid value x" occurs when a derived class constructor returns a value that is not an object or `undefined`.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#message)

-------------------------------------------------------------------------------------------------------------------

TypeError: Derived constructors may only return object or undefined (V8-based)
TypeError: derived class constructor returned invalid value 1 (Firefox)
TypeError: Cannot return a non-object type in the constructor of a derived class. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#error_type)

-------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------

Typically, a constructor does not need to return anything—the value of `this` is automatically returned when the class is constructed. A constructor can also return an object, and this object will override `this` as the newly constructed instance. However, returning something that's neither an object nor `undefined` is usually a mistake, because that value is ignored. In base classes and function constructors (using the `function` syntax), returning such a value is silently ignored, while in derived classes, it throws an error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#examples)

---------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#invalid_cases)

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
    
*   [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_derived_return/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/invalid_derived_return/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/invalid_derived_return (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FInvalid_derived_return&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Finvalid_derived_return%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FInvalid_derived_return%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Finvalid_derived_return%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")