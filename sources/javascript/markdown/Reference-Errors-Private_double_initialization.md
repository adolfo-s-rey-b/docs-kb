*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#mdn-search)
    

TypeError: Initializing an object twice is an error with private fields/methods
===============================================================================

The JavaScript exception "Initializing an object twice is an error with private fields/methods" occurs when an object that was created via a class constructor goes through the class construction again, and the class contains a [private element](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
. This is usually caused by the [return override](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#returning_overriding_object)
 trick.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#message)

--------------------------------------------------------------------------------------------------------------------------

TypeError: Cannot initialize #x twice on the same object (V8-based)
TypeError: Initializing an object twice is an error with private fields (Firefox)
TypeError: Cannot redefine existing private field (evaluating 'super(o)') (Safari)

TypeError: Cannot initialize private methods of class X twice on the same object (V8-based)
TypeError: Initializing an object twice is an error with private methods (Firefox)
TypeError: Cannot install same private methods on object more than once (evaluating 'super(o)') (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#error_type)

--------------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------------

For any object, if it already contains a private field or method, it would be an error to install the same field again. Private elements are installed on the value of `this` when the class constructor is called, so this error could happen if the `this` value is an already-constructed instance of this class.

Usually, `this` in a constructor is a newly created object which doesn't have any preexisting properties. However, it can be overridden by the return value of the base class. If the base class returns another object, that object would replace the current object as the value of `this`:

If you call `new Derived(anyObject)`, where `anyObject` is not an instance of `Derived`, the `Derived` constructor will be called with `anyObject` as the `this` value, and therefore install the `#x` private field on `anyObject`. This is the "return override" trick, which allows you to define arbitrary information on unrelated objects. However, if you call `new Derived(new Derived())`, or call `new Derived(anyObject)` again, the `Derived` constructor will try to install the `#x` private field again on an object which already has the `#x` private field, causing this error.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_double_initialization/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/private_double_initialization/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/private_double_initialization (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FPrivate_double_initialization&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fprivate_double_initialization%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FPrivate_double_initialization%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fprivate_double_initialization%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")