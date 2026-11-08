*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#mdn-search)
    

ReferenceError: super() called twice in derived class constructor
=================================================================

The JavaScript exception "super() called twice in derived class constructor" occurs when the [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 is called a second time for a given derived class constructor.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#message)

---------------------------------------------------------------------------------------------------------------

ReferenceError: Super constructor may only be called once (V8-based)
ReferenceError: super() called twice in derived class constructor (Firefox)
ReferenceError: 'super()' can't be called more than once in a constructor. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#error_type)

---------------------------------------------------------------------------------------------------------------------

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

The `super()` call can only be called at most once for each `new` call to a derived class constructor. This is because `super()` is responsible for initializing the parent class, and calling it more than once would result in the parent constructor being called multiple times.

The best way to prevent this is to ensure that `super()` is placed outside of any control flow structure. Otherwise, make sure that all code paths in the constructor lead to only one `super()` call.

The `super()` call can be "saved" in an arrow function nested within the constructor. Then, when you call the arrow function, you will also call `super()`, and the same rule applies: the arrow function can only be called at most once.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#examples)

-----------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#invalid_cases)

Sometimes the bug may be more subtle.

Originally, `flavors` may never simultaneously include both "chocolate" and "vanilla", but if that ever happens, the constructor will call `super()` twice. You need to rethink about how your class should be structured to avoid this issue.

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Super_called_twice/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/super_called_twice/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/super_called_twice (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FSuper_called_twice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fsuper_called_twice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FSuper_called_twice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fsuper_called_twice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")