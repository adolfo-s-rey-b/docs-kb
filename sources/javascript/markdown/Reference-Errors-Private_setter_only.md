*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#mdn-search)
    

TypeError: getting private setter-only property
===============================================

The JavaScript exception "getting private setter-only property" occurs when reading the value of a [private element](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 for which only a [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 is defined.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#message)

----------------------------------------------------------------------------------------------------------------

TypeError: '#x' was defined without a getter (V8-based)
TypeError: getting private setter-only property (Firefox)
TypeError: Trying to access an undefined private getter (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#error_type)

----------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------

There is an attempt to get the value of a private element for which only a [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 is specified. Unlike normal objects, where an undefined getter just means the property would always return undefined, for private elements, this is an error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#examples)

------------------------------------------------------------------------------------------------------------------

### [Private element with no getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#private_element_with_no_getter)

Here, `#name` has no getter, so trying to read it using `this.#name` will throw an error.

It's not usual for a private element to have a setter without a getter. Either add a getter or refactor your program so the setter can be removed too.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Private_setter_only/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/private_setter_only/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/private_setter_only (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FPrivate_setter_only&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fprivate_setter_only%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FPrivate_setter_only%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fprivate_setter_only%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")