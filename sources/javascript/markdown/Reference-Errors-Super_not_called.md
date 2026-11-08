*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#mdn-search)
    

ReferenceError: must call super constructor before using 'this' in derived class constructor
============================================================================================

The JavaScript exception "must call super constructor before using 'this' in derived class constructor" occurs when the [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 is not called for a given derived class constructor, and the derived constructor tries to access the value of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, or the derived constructor has already returned and the return value is not an object.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#message)

-------------------------------------------------------------------------------------------------------------

ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor (V8-based)
ReferenceError: must call super constructor before using 'this' in derived class constructor (Firefox)
ReferenceError: 'super()' must be called in derived constructor before accessing |this| or returning non-object. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#error_type)

-------------------------------------------------------------------------------------------------------------------

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------

The `super()` call can only be called at most once for each `new` call to a derived class constructor. Often, you need to call it exactly once, because if you don't call it, the parent constructor cannot initialize the value of `this`, so you cannot access `this` in the derived constructor and the `this` is not considered a valid constructed object (and throws if the derived constructor completes in this state). The way around it is to return an object from the derived class constructor, in which case the object returned will be used as the constructed object instead of `this`, allowing you to not call `super()`. This is rarely done though.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#examples)

---------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#invalid_cases)

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_not_called/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/super_not_called/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/super_not_called (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FSuper_not_called&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fsuper_not_called%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FSuper_not_called%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fsuper_not_called%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")