*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#mdn-search)
    

Function: prototype
===================

The **`prototype`** data property of a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 instance is used when the function is used as a constructor with the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator. It will become the new object's prototype.

**Note:** Not all [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 objects have the `prototype` property — see [description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#description)
.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#value)

-------------------------------------------------------------------------------------------------------------------

An object.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | no  |

**Note:** [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 are a type of function, so most of the description here applies to the `prototype` property of classes too. The only salient difference is that the `prototype` property of a class is not writable.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#description)

-------------------------------------------------------------------------------------------------------------------------------

When a function is called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, the constructor's `prototype` property will become the resulting object's prototype.

You can read [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain#constructors)
 for more information about the interactions between a constructor function's `prototype` property and the resulting object's prototype.

A function having a `prototype` property is not sufficient for it to be eligible as a constructor. [Generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 have a `prototype` property, but cannot be called with `new`:

Instead, generator functions' `prototype` property is used when they are called _without_ `new`. The `prototype` property will become the returned [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
 object's prototype.

In addition, some functions may have a `prototype` but throw unconditionally when called with `new`. For example, the [`Symbol()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/Symbol)
 and [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 functions throw when called with `new`, because `Symbol.prototype` and `BigInt.prototype` are only intended to provide methods for the primitive values, but the wrapper objects should not be directly constructed.

The following functions do not have `prototype`, and are therefore ineligible as constructors, even if a `prototype` property is later manually assigned:

The following are valid constructors that have `prototype`:

A [bound function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 does not have a `prototype` property, but may be constructable. When it's constructed, the target function is constructed instead, and if the target function is constructable, it would return a normal instance.

A function's `prototype` property, by default, is a plain object with one property: [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
, which is a reference to the function itself. The `constructor` property is writable, non-enumerable, and configurable.

If the `prototype` of a function is reassigned with something other than an [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
, when the function is called with `new`, the returned object's prototype would be `Object.prototype` instead. (In other words, `new` ignores the `prototype` property and constructs a plain object.)

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Changing the prototype of all instances by mutating the prototype property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#changing_the_prototype_of_all_instances_by_mutating_the_prototype_property)

### [Adding a non-method property to a class's prototype property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#adding_a_non-method_property_to_a_classs_prototype_property)

[Class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
 add properties to each instance. Class methods declare _function_ properties on the prototype. However, there's no way to add a non-function property to the prototype. In case you want to share static data between all instances (for example, [`Error.prototype.name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/name)
 is the same between all error instances), you can manually assign it on the `prototype` of a class.

This can be made more ergonomic using [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
, which are called when the class is initialized.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-instances-prototype](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-function-instances-prototype) |

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    
*   [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain#constructors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/function/prototype/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/function/prototype (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fprototype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fprototype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fprototype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fprototype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")