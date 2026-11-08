*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#mdn-search)
    

instanceof
==========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`instanceof`** operator tests to see if the `prototype` property of a constructor appears anywhere in the prototype chain of an object. The return value is a boolean value. Its behavior can be customized with [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#try_it)

--------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#syntax)

--------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#parameters)

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#object)

The object to test.

[`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#constructor)

Constructor to test against.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if `constructor` is not an object. If `constructor` doesn't have a [`[Symbol.hasInstance]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
 method, it must also be a function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#description)

------------------------------------------------------------------------------------------------------------------

The `instanceof` operator tests the presence of `constructor.prototype` in `object`'s prototype chain. This usually (though [not always](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#overriding_the_behavior_of_instanceof)
) means `object` was constructed with `constructor`.

Note that the value of an `instanceof` test can change if `constructor.prototype` is re-assigned after creating the object (which is usually discouraged). It can also be changed by changing `object`'s prototype using [`Object.setPrototypeOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
.

Classes behave in the same way, because classes also have the `prototype` property.

For [bound functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
, `instanceof` looks up for the `prototype` property on the target function, since bound functions don't have `prototype`.

### [instanceof and Symbol.hasInstance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#instanceof_and_symbol.hasinstance)

If `constructor` has a [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
 method, the method will be called in priority, with `object` as its only argument and `constructor` as `this`.

Because all functions inherit from `Function.prototype` by default, most of the time, the [`Function.prototype[Symbol.hasInstance]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Symbol.hasInstance)
 method specifies the behavior of `instanceof` when the right-hand side is a function. See the [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
 page for the exact algorithm of `instanceof`.

### [instanceof and multiple realms](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#instanceof_and_multiple_realms)

JavaScript execution environments (windows, frames, etc.) are each in their own _realm_. This means that they have different built-ins (different global object, different constructors, etc.). This may result in unexpected results. For instance, `[] instanceof window.frames[0].Array` will return `false`, because `Array.prototype !== window.frames[0].Array.prototype` and arrays in the current realm inherit from the former.

This may not make sense at first, but for scripts dealing with multiple frames or windows, and passing objects from one context to another via functions, this will be a valid and strong issue. For instance, you can securely check if a given object is in fact an Array using [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)
, neglecting which realm it comes from.

For example, to check if a [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node)
 is an [`SVGElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGElement)
 in a different context, you can use `myNode instanceof myNode.ownerDocument.defaultView.SVGElement`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#examples)

------------------------------------------------------------------------------------------------------------

### [Using instanceof with String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#using_instanceof_with_string)

The following example shows the behavior of `instanceof` with `String` objects.

### [Using instanceof with Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#using_instanceof_with_map)

The following example shows the behavior of `instanceof` with `Map` objects.

### [Objects created using Object.create()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#objects_created_using_object.create)

The following example shows the behavior of `instanceof` with objects created using [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
.

### [Demonstrating that myCar is of type Car and type Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#demonstrating_that_mycar_is_of_type_car_and_type_object)

The following code creates an object type `Car` and an instance of that object type, `myCar`. The `instanceof` operator demonstrates that the `myCar` object is of type `Car` and of type `Object`.

### [Not an instanceof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#not_an_instanceof)

To test if an object is not an `instanceof` a specific constructor, you can do:

This is really different from:

This will always be `false`. (`!myCar` will be evaluated before `instanceof`, so you always try to know if a boolean is an instance of `Car`).

### [Overriding the behavior of instanceof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#overriding_the_behavior_of_instanceof)

A common pitfall of using `instanceof` is believing that, if `x instanceof C`, then `x` was created using `C` as constructor. This is not true, because `x` could be directly assigned with `C.prototype` as its prototype. In this case, if your code reads [private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 of `C` from `x`, it would still fail:

To avoid this, you can override the behavior of `instanceof` by adding a `Symbol.hasInstance` method to `C`, so that it does a branded check with [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
:

Note that you may want to limit this behavior to the current class; otherwise, it could lead to false positives for subclasses:

You could do this by checking that `this` is the current constructor:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-relational-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-relational-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof#see_also)

------------------------------------------------------------------------------------------------------------

*   [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
    
*   [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
    
*   [`Object.prototype.isPrototypeOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isPrototypeOf)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/instanceof/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/instanceof (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Finstanceof&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Finstanceof%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Finstanceof%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Finstanceof%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")