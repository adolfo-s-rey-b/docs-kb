*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#mdn-search)
    

AbstractModuleSource
====================

An **_AbstractModuleSource_** object represents the compiled source of a module obtained with [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
 or [`import.source()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source)
. There is no directly visible `AbstractModuleSource` constructor.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#description)

---------------------------------------------------------------------------------------------------------------------------------

The `AbstractModuleSource` constructor (often referred to as `%AbstractModuleSource%` to indicate its "intrinsicness", since it does not correspond to any global exposed to a JavaScript program) serves as the superclass of all module source subclasses, providing a common interface of utility methods. This constructor is not directly exposed: there is no global `AbstractModuleSource` property. It is only accessible through `Object.getPrototypeOf(moduleSourceObject.constructor)` and similar.

### [AbstractModuleSource objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#abstractmodulesource_objects)

*   [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module)
    

JavaScript module source objects will be added by the [ECMAScript Module Phase Imports](https://github.com/tc39/proposal-esm-phase-imports "External link (opens in new tab)")
 proposal.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#constructor)

---------------------------------------------------------------------------------------------------------------------------------

This object cannot be instantiated directly — attempting to construct it with `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

js

    import source modSource from "./module.wasm";
    
    new (Object.getPrototypeOf(modSource.constructor))();
    // TypeError: Abstract class AbstractModuleSource not directly constructable
    

Instead, obtain a module source object using `import source`, `import.source()`, or a concrete module type's API, such as `WebAssembly.Module()`. These mechanisms do not call the abstract constructor.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#instance_properties)

-------------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `AbstractModuleSource.prototype` and shared by all `AbstractModuleSource` subclass instances.

[`AbstractModuleSource.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. `AbstractModuleSource.prototype.constructor` is the hidden `AbstractModuleSource` constructor function, but each module source subclass also defines its own `constructor` property.

[`AbstractModuleSource.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#abstractmodulesource.prototypesymbol.tostringtag)

The initial value of the [`AbstractModuleSource.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is a getter that returns a string based on the constructor's identity, such as `"WebAssembly.Module"` or `"ModuleSource"`. It returns `undefined` if the `this` value is not an instance of one of the module source subclasses. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Source Phase Imports  <br>\# sec-module-source-objects](https://tc39.es/proposal-source-phase-imports/#sec-module-source-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module)
    
*   [`import.source()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source)
    
*   [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/abstractmodulesource/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/abstractmodulesource (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAbstractModuleSource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fabstractmodulesource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAbstractModuleSource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fabstractmodulesource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F31bad7cd99cccf47f6332b81bbff4371e2bc551f%0A*+Document+last+modified%3A+2026-09-11T01%3A04%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")