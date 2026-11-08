*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#mdn-search)
    

TypeError: setting getter-only property "x"
===========================================

The JavaScript [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
\-only exception "setting getter-only property" occurs when there is an attempt to set a new value to a property for which only a [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 is specified, or when setting a [private accessor property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 that similarly only has a getter defined.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#message)

--------------------------------------------------------------------------------------------------------

TypeError: Cannot set property x of #<Object> which has only a getter (V8-based)
TypeError: '#x' was defined without a setter (V8-based)
TypeError: setting getter-only property "x" (Firefox)
TypeError: Attempted to assign to readonly property. (Safari)
TypeError: Trying to access an undefined private setter (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#error_type)

--------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 only.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------

There is an attempt to set a new value to a property for which only a [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 is specified. While this will be silently ignored in non-strict mode, it will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. Classes are always in strict mode, so assigning to a getter-only private element always throws this error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#examples)

----------------------------------------------------------------------------------------------------------

### [Property with no setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#property_with_no_setter)

The example below shows how to set a getter for a property. It doesn't specify a [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
, so a `TypeError` will be thrown upon trying to set the `temperature` property to `30`. For more details see also the [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 page.

To fix this error, you will either need to remove the `arc.temperature = 30` line, which attempts to set the temperature property, or you will need to implement a [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 for it, for example like this:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only#see_also)

----------------------------------------------------------------------------------------------------------

*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    
*   [`Object.defineProperties()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_only/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/getter_only/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/getter_only (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGetter_only&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fgetter_only%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGetter_only%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fgetter_only%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")