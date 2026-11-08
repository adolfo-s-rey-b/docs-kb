*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#mdn-search)
    

TypeError: "x" is read-only
===========================

The JavaScript [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
\-only exception "is read-only" occurs when a global variable or object property that was assigned to is a read-only property.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#message)

------------------------------------------------------------------------------------------------------

TypeError: Cannot assign to read only property 'x' of #<Object> (V8-based)
TypeError: "x" is read-only (Firefox)
TypeError: Attempted to assign to readonly property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#error_type)

------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 only.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------

The global variable or object property that was assigned to is a read-only property. (Technically, it is a [non-writable data property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty#writable_attribute)
.)

This error happens only in [strict mode code](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. In non-strict code, the assignment is silently ignored.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#examples)

--------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#invalid_cases)

Read-only properties are not super common, but they can be created using [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 or [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
.

js

    "use strict";
    const obj = Object.freeze({ name: "Elsa", score: 157 });
    obj.score = 0; // TypeError
    
    ("use strict");
    Object.defineProperty(this, "LUNG_COUNT", { value: 2, writable: false });
    LUNG_COUNT = 3; // TypeError
    
    ("use strict");
    const frozenArray = Object.freeze([0, 1, 2]);
    frozenArray[0]++; // TypeError
    

There are also a few read-only properties built into JavaScript. Maybe you tried to redefine a mathematical constant.

js

    "use strict";
    Math.PI = 4; // TypeError
    

Sorry, you can't do that.

The global variable `undefined` is also read-only, so you can't silence the infamous "undefined is not a function" error by doing this:

js

    "use strict";
    undefined = function () {}; // TypeError: "undefined" is read-only
    

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#valid_cases)

js

    "use strict";
    let obj = Object.freeze({ name: "Score", points: 157 });
    obj = { name: obj.name, points: 0 }; // replacing it with a new object works
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only#see_also)

--------------------------------------------------------------------------------------------------------

*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    
*   [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Read-only/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/read-only/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/read-only (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRead-only&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fread-only%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRead-only%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fread-only%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")