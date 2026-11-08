*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#mdn-search)
    

Function: name
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`name`** data property of a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 instance indicates the function's name as specified when it was created, or it may be either `anonymous` or `''` (an empty string) for functions created anonymously.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#try_it)

----------------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#value)

--------------------------------------------------------------------------------------------------------------

A string.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | yes |

**Note:** In non-standard, pre-ES2015 implementations the `configurable` attribute was `false` as well.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#description)

--------------------------------------------------------------------------------------------------------------------------

The function's `name` property can be used to identify the function in debugging tools or error messages. It has no semantic significance to the language itself.

The `name` property is read-only and cannot be changed by the assignment operator:

To change it, use [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
.

The `name` property is typically inferred from how the function is defined. In the following sections, we will describe the various ways in which it can be inferred.

### [Function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#function_declaration)

The `name` property returns the name of a function declaration.

### [Default-exported function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#default-exported_function_declaration)

An [`export default`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
 declaration exports the function as a declaration instead of an expression. If the declaration is anonymous, the name is `"default"`.

### [Function constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#function_constructor)

Functions created with the [`Function()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
 constructor have name "anonymous".

### [Function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#function_expression)

If the function expression is named, that name is used as the `name` property.

Anonymous function expressions, created using either the `function` keyword or the arrow function syntax, have `""` (an empty string) as their name by default.

However, such cases are rare — usually, in order to call the function elsewhere, the function expression is associated with an identifier. The name of an anonymous function expression can be inferred within certain syntactic contexts, including: [variable declaration, method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#variable_declaration_and_method)
, [initializer, and default value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#initializer_and_default_value)
.

One practical case where the name cannot be inferred is a function returned from another function:

### [Variable declaration and method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#variable_declaration_and_method)

Variables and methods can infer the name of an anonymous function from its syntactic position.

The same applies to assignment:

### [Initializer and default value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#initializer_and_default_value)

Functions in initializers (default values) of [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#default_value)
, [default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
, [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
, etc., will inherit the name of the bound identifier as their `name`.

### [Shorthand method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#shorthand_method)

### [Bound function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#bound_function)

[`Function.prototype.bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 produces a function whose name is "bound " plus the function name.

### [Getter and setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#getter_and_setter)

When using [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 accessor properties, "get" or "set" will appear in the function name.

### [Class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#class)

A class's name follows the same algorithm as function declarations and expressions.

**Warning:** JavaScript will set the function's `name` property only if a function does not have an own property called `name`. However, classes' [static members](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 will be set as own properties of the class constructor function, and thus prevent the built-in `name` from being applied. See [an example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#telling_the_constructor_name_of_an_object)
 below.

### [Symbol as function name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#symbol_as_function_name)

If a [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
 is used a function name and the symbol has a description, the method's name is the description in square brackets.

### [Private fields and methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#private_fields_and_methods)

Private fields and private methods have the hash (`#`) as part of their names.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#examples)

--------------------------------------------------------------------------------------------------------------------

### [Telling the constructor name of an object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#telling_the_constructor_name_of_an_object)

You can use `obj.constructor.name` to check the "class" of an object.

However, because static members will become own properties of the class, we can't obtain the class name for virtually any class with a static method property `name()`:

With a `static name()` method `Foo.name` no longer holds the actual class name but a reference to the `name()` function object. Trying to obtain the class of `fooInstance` via `fooInstance.constructor.name` won't give us the class name at all, but instead a reference to the static class method. Example:

Due to the existence of static fields, `name` may not be a function either.

If a class has a static property called `name`, it will also become _writable_. The built-in definition in the absence of a custom static definition is _read-only_:

Therefore you may not rely on the built-in `name` property to always hold a class's name.

### [JavaScript compressors and minifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#javascript_compressors_and_minifiers)

**Warning:** Be careful when using the `name` property with source-code transformations, such as those carried out by JavaScript compressors (minifiers) or obfuscators. These tools are often used as part of a JavaScript build pipeline to reduce the size of a program prior to deploying it to production. Such transformations often change a function's name at build time.

Source code such as:

may be compressed to:

In the uncompressed version, the program runs into the truthy branch and logs "'foo' is an instance of 'Foo'" — whereas, in the compressed version it behaves differently, and runs into the else branch. If you rely on the `name` property, like in the example above, make sure your build pipeline doesn't change function names, or don't assume a function has a particular name.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-instances-name](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-function-instances-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill for `Function: name` in `core-js`](https://core-js.io/docs/features/ecmascript/function "External link (opens in new tab)")
    
*   [es-shims polyfill of `Function.prototype.name`](https://www.npmjs.com/package/function.prototype.name "External link (opens in new tab)")
    
*   [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/function/name/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/function/name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fname&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fname%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fname%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fname%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")