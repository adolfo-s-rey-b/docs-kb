*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#mdn-search)
    

TypeError: can't set prototype of this object
=============================================

The JavaScript exception "can't set prototype of this object" occurs when attempting to set the prototype of an object, but the object's prototype is frozen, either by being a built-in immutable prototype object, or by being [non-extensible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#message)

---------------------------------------------------------------------------------------------------------------

TypeError: Immutable prototype object 'Object.prototype' cannot have their prototype set (V8-based)
TypeError: #<Object> is not extensible (V8-based)
TypeError: can't set prototype of this object (Firefox)
TypeError: Cannot set prototype of immutable prototype object (Safari)
TypeError: Attempted to assign to readonly property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#error_type)

---------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

You are using one of the prototype-mutating methods—most notably, [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
—on an object whose prototype is immutable. Some built-in objects have immutable prototypes, such as `Object.prototype` and [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
, for security reasons. User objects can also prevent prototype changes by using [`Object.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)
, [`Object.seal()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)
, or [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#examples)

-----------------------------------------------------------------------------------------------------------------

### [Changing the prototype of a built-in object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#changing_the_prototype_of_a_built-in_object)

A selected few built-in objects have immutable prototypes. For example, you cannot change the prototype of `Object.prototype`:

This prevents you from being able to arbitrarily change the behavior of all objects in the system. The prototype of `Object.prototype` is always `null`. However, other built-in prototype objects, such as `Function.prototype` and `Array.prototype`, are not protected by default in this regard.

### [Changing the prototype of a non-extensible object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#changing_the_prototype_of_a_non-extensible_object)

If you make an object non-extensible, you cannot change its prototype either:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
    
*   [`Object.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_set_prototype/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_set_prototype/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_set_prototype (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_set_prototype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_set_prototype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_set_prototype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_set_prototype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")