*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#mdn-search)
    

delete
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`delete`** operator removes a property from an object. If the property's value is an object and there are no more references to the object, the object held by that property is eventually released automatically.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#syntax)

----------------------------------------------------------------------------------------------------

**Note:** The syntax allows a wider range of expressions following the `delete` operator, but only the above forms lead to meaningful behaviors.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#parameters)

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#object)

The name of an object, or an expression evaluating to an object.

[`property`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#property)

The property to delete.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#return_value)

`true` for all cases except when the property is an [own](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 [non-configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty#configurable_attribute)
 property, in which case `false` is returned in non-strict mode.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 if the property is an own non-configurable property.

[`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

Thrown if `object` is [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#description)

--------------------------------------------------------------------------------------------------------------

The `delete` operator has the same [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 as other unary operators like [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
. Therefore, it accepts any expression formed by higher-precedence operators. However, the following forms lead to early syntax errors in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
:

Because [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 are automatically in strict mode, and [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 can only be legally referenced in class bodies, this means private elements can never be deleted. While `delete identifier` [may work](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#deleting_global_properties)
 if `identifier` refers to a configurable property of the global object, you should avoid this form and prefix it with [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
 instead.

While other expressions are accepted, they don't lead to meaningful behaviors:

The `delete` operator removes a given property from an object. On successful deletion, it will return `true`, else `false` will be returned. Unlike what common belief suggests (perhaps due to other programming languages like [delete in C++](https://learn.microsoft.com/en-us/cpp/cpp/delete-operator-cpp?view=msvc-170 "External link (opens in new tab)")
), the `delete` operator has **nothing** to do with directly freeing memory. Memory management is done indirectly via breaking references. See the [memory management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management)
 page for more details.

It is important to consider the following scenarios:

*   If the property which you are trying to delete does not exist, `delete` will not have any effect and will return `true`.
*   `delete` only has an effect on own properties. If a property with the same name exists on the object's prototype chain, then after deletion, the object will use the property from the prototype chain.
*   Non-configurable properties cannot be removed. This includes properties of built-in objects like [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
    , [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    , [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
     and properties that are created as non-configurable with methods like [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    .
*   Deleting variables, including function parameters, never works. `delete variable` will throw a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
     in strict mode, and will have no effect in non-strict mode.
    *   Any variable declared with [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
         cannot be deleted from the global scope or from a function's scope, because while they may be attached to the [global object](https://developer.mozilla.org/en-US/docs/Glossary/Global_object)
        , they are not configurable.
    *   Any variable declared with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
         or [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
         cannot be deleted from the scope within which they were defined, because they are not attached to an object.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#examples)

--------------------------------------------------------------------------------------------------------

### [Using delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#using_delete)

**Note:** The following example uses non-strict-mode only features, like implicitly creating global variables and deleting identifiers, which are forbidden in strict mode.

### [delete and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#delete_and_the_prototype_chain)

In the following example, we delete an own property of an object while a property with the same name is available on the prototype chain:

### [Deleting array elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#deleting_array_elements)

When you delete an array element, the array `length` is not affected. This holds even if you delete the last element of the array.

When the `delete` operator removes an array element, that element is no longer in the array. In the following example, `trees[3]` is removed with `delete`.

This creates a [sparse array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
 with an empty slot. If you want an array element to exist but have an undefined value, use the `undefined` value instead of the `delete` operator. In the following example, `trees[3]` is assigned the value `undefined`, but the array element still exists:

If instead, you want to remove an array element by changing the contents of the array, use the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method. In the following example, `trees[3]` is removed from the array completely using [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
:

### [Deleting non-configurable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#deleting_non-configurable_properties)

When a property is marked as non-configurable, `delete` won't have any effect, and will return `false`. In strict mode, this will raise a `TypeError`.

[`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
 creates non-configurable properties that cannot be deleted with the `delete` operator:

In strict mode, this would raise an exception.

### [Deleting global properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#deleting_global_properties)

If a global property is configurable (for example, via direct property assignment), it can be deleted, and subsequent references to them as global variables will produce a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-delete-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-delete-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#see_also)

--------------------------------------------------------------------------------------------------------

*   [`Reflect.deleteProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/deleteProperty)
    
*   [`Map.prototype.delete()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/delete)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 17, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/delete/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/delete (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fdelete&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdelete%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fdelete%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdelete%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F03d5115691a7a9fa3df3b6ebd20a0c7eed213252%0A*+Document+last+modified%3A+2025-07-17T10%3A30%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")