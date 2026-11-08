*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#mdn-search)
    

InternalError: too much recursion
=================================

The JavaScript exception "too much recursion" or "Maximum call stack size exceeded" occurs when there are too many function calls, or a function is missing a base case.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#message)

---------------------------------------------------------------------------------------------------------------

RangeError: Maximum call stack size exceeded (Chrome)
InternalError: too much recursion (Firefox)
RangeError: Maximum call stack size exceeded. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#error_type)

---------------------------------------------------------------------------------------------------------------------

[`InternalError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)
 in Firefox; [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 in Chrome and Safari.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

A function that calls itself is called a _recursive function_. Once a condition is met, the function stops calling itself. This is called a _base case_.

In some ways, recursion is analogous to a loop. Both execute the same code multiple times, and both require a condition (to avoid an infinite loop, or rather, infinite recursion in this case). When there are too many function calls, or a function is missing a base case, JavaScript will throw this error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#examples)

-----------------------------------------------------------------------------------------------------------------

This recursive function runs 10 times, as per the exit condition.

Setting this condition to an extremely high value, won't work:

This recursive function is missing a base case. As there is no exit condition, the function will call itself infinitely.

### [Class error: too much recursion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#class_error_too_much_recursion)

When a value is assigned to the property name (this.name = name;) JavaScript needs to set that property. When this happens, the setter function is triggered.

In this example when the setter is triggered, it is told to do the same thing again: _to set the same property that it is meant to handle._ This causes the function to call itself, again and again, making it infinitely recursive.

This issue also appears if the same variable is used in the getter.

To avoid this problem, make sure that the property being assigned to inside the setter function is different from the one that initially triggered the setter. The same goes for the getter.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Recursion](https://developer.mozilla.org/en-US/docs/Glossary/Recursion)
    
*   [Recursive functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#recursion)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Too_much_recursion/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/too_much_recursion/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/too_much_recursion (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FToo_much_recursion&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Ftoo_much_recursion%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FToo_much_recursion%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Ftoo_much_recursion%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")