*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#mdn-search)
    

TypeError: property "x" is non-configurable and can't be deleted
================================================================

The JavaScript exception "property is non-configurable and can't be deleted" occurs when it was attempted to delete a property, but that property is [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#message)

--------------------------------------------------------------------------------------------------------

TypeError: Cannot delete property 'x' of #<Object> (V8-based)
TypeError: property "x" is non-configurable and can't be deleted (Firefox)
TypeError: Unable to delete property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#error_type)

--------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 in strict mode only.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------

It was attempted to delete a property, but that property is [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
. The `configurable` attribute controls whether the property can be deleted from the object and whether its attributes (other than `writable`) can be changed.

This error happens only in [strict mode code](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. In non-strict code, the operation returns `false`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#examples)

----------------------------------------------------------------------------------------------------------

### [Attempting to delete non-configurable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#attempting_to_delete_non-configurable_properties)

Non-configurable properties are not super common, but they can be created using [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 or [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
.

js

    "use strict";
    const obj = Object.freeze({ name: "Elsa", score: 157 });
    delete obj.score; // TypeError
    

js

    "use strict";
    const obj = {};
    Object.defineProperty(obj, "foo", { value: 2, configurable: false });
    delete obj.foo; // TypeError
    

js

    "use strict";
    const frozenArray = Object.freeze([0, 1, 2]);
    frozenArray.pop(); // TypeError
    

There are also a few non-configurable properties built into JavaScript. Maybe you tried to delete a mathematical constant.

js

    "use strict";
    delete Math.PI; // TypeError
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete#see_also)

----------------------------------------------------------------------------------------------------------

*   [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
    
*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    
*   [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_delete/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_delete/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_delete (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_delete&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_delete%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_delete%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_delete%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")