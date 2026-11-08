*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#mdn-search)
    

TypeError: can't redefine non-configurable property "x"
=======================================================

The JavaScript exception "can't redefine non-configurable property" occurs when it was attempted to redefine a property, but that property is [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#message)

-------------------------------------------------------------------------------------------------------------------

TypeError: Cannot redefine property: "x" (V8-based)
TypeError: can't redefine non-configurable property "x" (Firefox)
TypeError: Attempting to change value of a readonly property. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#error_type)

-------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------

It was attempted to redefine a property, but that property is [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
. The `configurable` attribute controls whether the property can be deleted from the object and whether its attributes (other than `writable`) can be changed. Usually, properties in an object created by an [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 are configurable. However, for example, when using [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
, the property isn't configurable by default.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#examples)

---------------------------------------------------------------------------------------------------------------------

### [Non-configurable properties created by Object.defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#non-configurable_properties_created_by_object.defineproperty)

The [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 creates non-configurable properties if you haven't specified them as configurable.

js

    const obj = Object.create({});
    Object.defineProperty(obj, "foo", { value: "bar" });
    
    Object.defineProperty(obj, "foo", { value: "baz" });
    // TypeError: can't redefine non-configurable property "foo"
    

You will need to set the "foo" property to configurable, if you intend to redefine it later in the code.

js

    const obj = Object.create({});
    Object.defineProperty(obj, "foo", { value: "bar", configurable: true });
    Object.defineProperty(obj, "foo", { value: "baz", configurable: true });
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [\[\[Configurable\]\]](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
    
*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_redefine_property/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_redefine_property/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_redefine_property (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_redefine_property&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_redefine_property%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_redefine_property%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_redefine_property%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")