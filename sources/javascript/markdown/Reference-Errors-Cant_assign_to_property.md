*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#mdn-search)
    

TypeError: can't assign to property "x" on "y": not an object
=============================================================

The JavaScript strict mode exception "can't assign to property" occurs when attempting to create a property on [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 value such as a [symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
, a [string](https://developer.mozilla.org/en-US/docs/Glossary/String)
, a [number](https://developer.mozilla.org/en-US/docs/Glossary/Number)
 or a [boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)
. [Primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 values cannot hold any [property](https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#message)

--------------------------------------------------------------------------------------------------------------------

TypeError: Cannot create property 'x' on number '1' (V8-based)
TypeError: can't assign to property "x" on 1: not an object (Firefox)
TypeError: Attempted to assign to readonly property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#error_type)

--------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is raised when attempting to create a property on [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 value such as a [symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
, a [string](https://developer.mozilla.org/en-US/docs/Glossary/String)
, a [number](https://developer.mozilla.org/en-US/docs/Glossary/Number)
 or a [boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)
. [Primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 values cannot hold any [property](https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript)
.

The problem might be that an unexpected value is flowing at an unexpected place, or that an object variant of a [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 or a [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
 is expected.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#examples)

----------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#invalid_cases)

### [Fixing the issue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#fixing_the_issue)

Either fix the code to prevent the [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 from being used in such places, or fix the issue by creating the object equivalent [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    
*   [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_assign_to_property/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_assign_to_property/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_assign_to_property (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_assign_to_property&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_assign_to_property%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_assign_to_property%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_assign_to_property%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")