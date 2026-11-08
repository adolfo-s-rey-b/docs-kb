*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#mdn-search)
    

Object.prototype.constructor
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`constructor`** data property of an [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 instance returns a reference to the constructor function that created the instance object. Note that the value of this property is a reference to _the function itself_, not a string containing the function's name.

**Note:** This is a property of JavaScript objects. For the `constructor` method in classes, see [its own reference page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#value)

-------------------------------------------------------------------------------------------------------------------

A reference to the constructor function that created the instance object.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | yes |

**Note:** This property is created by default on the [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property of every constructor function and is inherited by all objects created by that constructor.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#description)

-------------------------------------------------------------------------------------------------------------------------------

Any object (with the exception of [`null` prototype objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
) will have a `constructor` property on its `[[Prototype]]`. Objects created with literals will also have a `constructor` property that points to the constructor type for that object — for example, array literals create [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 objects, and [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 create plain objects.

Note that `constructor` usually comes from the constructor's [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property. If you have a longer prototype chain, you can usually expect every object in the chain to have a `constructor` property.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Displaying the constructor of an object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#displaying_the_constructor_of_an_object)

The following example creates a constructor (`Tree`) and an object of that type (`theTree`). The example then displays the `constructor` property for the object `theTree`.

This example displays the following output:

theTree.constructor is function Tree(name) {
  this.name = name;
}

### [Assigning the constructor property to an object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#assigning_the_constructor_property_to_an_object)

One can assign the `constructor` property of non-primitives.

This does not overwrite the old `constructor` property — it was originally present on the instance's `[[Prototype]]`, not as its own property.

But even when `Object.getPrototypeOf(a).constructor` is re-assigned, it won't change other behaviors of the object. For example, the behavior of `instanceof` is controlled by [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
, not `constructor`:

There is nothing protecting the `constructor` property from being re-assigned or shadowed, so using it to detect the type of a variable should usually be avoided in favor of less fragile ways like `instanceof` and [`Symbol.toStringTag`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 for objects, or [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
 for primitives.

### [Changing the constructor of a constructor function's prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#changing_the_constructor_of_a_constructor_functions_prototype)

Every constructor has a [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property, which will become the instance's `[[Prototype]]` when called via the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator. `ConstructorFunction.prototype.constructor` will therefore become a property on the instance's `[[Prototype]]`, as previously demonstrated.

However, if `ConstructorFunction.prototype` is re-assigned, the `constructor` property will be lost. For example, the following is a common way to create an inheritance pattern:

The `constructor` of instances of `Child` will be `Parent` due to `Child.prototype` being re-assigned.

This is usually not a big deal — the language almost never reads the `constructor` property of an object. The only exception is when using [`[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/species)
 to create new instances of a class, but such cases are rare, and you should be using the [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 syntax to subclass builtins anyway.

However, ensuring that `Child.prototype.constructor` always points to `Child` itself is crucial when some caller is using `constructor` to access the original class from an instance. Take the following case: the object has the `create()` method to create itself.

In the example above, an exception is thrown, since the `constructor` links to `Parent`. To avoid this, just assign the necessary constructor you are going to use.

Note that when manually adding the `constructor` property, it's crucial to make the property [non-enumerable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
, so `constructor` won't be visited in [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loops — as it normally isn't.

If the code above looks like too much boilerplate, you may also consider using [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
 to manipulate the prototype chain.

`Object.setPrototypeOf()` comes with its potential performance downsides because all previously created objects involved in the prototype chain have to be re-compiled; but if the above initialization code happens before `Parent` or `CreatedConstructor` are constructed, the effect should be minimal.

Let's consider one more involved case.

For this example to work properly, we can reassign the `Parent`'s static properties to `Child`:

But even better, we can make the constructor functions themselves extend each other, as classes' [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 do.

Again, using `Object.setPrototypeOf()` may have adverse performance effects, so make sure it happens immediately after the constructor declaration and before any instances are created — to avoid objects being "tainted".

**Note:** Manually updating or setting the constructor can lead to different and sometimes confusing consequences. To prevent this, just define the role of `constructor` in each specific case. In most cases, `constructor` is not used and reassigning it is not necessary.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object.prototype.constructor](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-object.prototype.constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
    
*   [Constructor](https://developer.mozilla.org/en-US/docs/Glossary/Constructor)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/object/constructor/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/object/constructor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fconstructor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fconstructor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fconstructor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fconstructor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")