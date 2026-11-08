*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#mdn-search)
    

SyntaxError: use of super property/member accesses only valid within methods or eval code within methods
========================================================================================================

The JavaScript exception "use of super property/member accesses only valid within methods or eval code within methods" occurs when the [`super.x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 or `super[x]` syntax is used outside of a [method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#message)

-----------------------------------------------------------------------------------------------------------

SyntaxError: 'super' keyword unexpected here (V8-based)
SyntaxError: use of super property accesses only valid within methods or eval code within methods (Firefox)
SyntaxError: super is not valid in this context. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#error_type)

-----------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------

The `super.x` syntax is used to access properties on the prototype of the current object. It can be used in methods of both [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 and [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
, [field initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
, and [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
, but not in other contexts.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#examples)

-------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#invalid_cases)

You can't use `super.x` outside of a method in an object:

You can't use `super.x` in a function, even if that function has the effect of being a method:

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#valid_cases)

You can use `super.x` in a method:

You can use `super.x` in a field initializer:

You can use `super.x` in object methods too:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_super_prop/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bad_super_prop/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bad_super_prop (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_super_prop&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_super_prop%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_super_prop%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_super_prop%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")