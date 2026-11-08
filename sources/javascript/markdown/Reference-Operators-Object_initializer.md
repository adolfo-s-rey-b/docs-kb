*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#mdn-search)
    

Object initializer
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

An **object initializer** is a comma-delimited list of zero or more pairs of property names and associated values of an object, enclosed in curly braces (`{}`). Objects can also be initialized using [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
 or [by invoking a constructor function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#using_a_constructor_function)
 with the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#try_it)

----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#syntax)

----------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#description)

--------------------------------------------------------------------------------------------------------------------------

An object initializer is an expression that describes the initialization of an [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
. Objects consist of _properties_, which are used to describe an object. The values of object properties can either contain [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 data types or other objects.

### [Object literal syntax vs. JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#object_literal_syntax_vs._json)

The object literal syntax is not the same as the **J**ava**S**cript **O**bject **N**otation ([JSON](https://developer.mozilla.org/en-US/docs/Glossary/JSON)
). Although they look similar, there are differences between them:

*   JSON _only_ permits property definition using the `"property": value` syntax. The property name must be double-quoted, and the definition cannot be a shorthand. Computed property names are not allowed either.
*   JSON object property values can only be strings, numbers, `true`, `false`, `null`, arrays, or another JSON object. This means JSON cannot express methods or non-plain objects like [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
     or [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
    .
*   In JSON, `"__proto__"` is a normal property key. In an object literal, it [sets the object's prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#prototype_setter)
    .

JSON is a _strict subset_ of the object literal syntax, meaning that every valid JSON text can be parsed as an object literal, and would likely not cause syntax errors. The only exception is that the object literal syntax prohibits duplicate `__proto__` keys, which does not apply to [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
. The latter treats `__proto__` like a normal property and takes the last occurrence as the property's value. The only time when the object value they represent (a.k.a. their semantic) differ is also when the source contains the `__proto__` key — for object literals, it sets the object's prototype; for JSON, it's a normal property.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#examples)

--------------------------------------------------------------------------------------------------------------------

### [Creating objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#creating_objects)

An empty object with no properties can be created like this:

However, the advantage of the _literal_ or _initializer_ notation is, that you are able to quickly create objects with properties inside the curly braces. You notate a list of `key: value` pairs delimited by commas.

The following code creates an object with three properties and the keys are `"foo"`, `"age"` and `"baz"`. The values of these keys are a string `"bar"`, the number `42`, and another object.

### [Accessing properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#accessing_properties)

Once you have created an object, you might want to read or change them. Object properties can be accessed by using the dot notation or the bracket notation. (See [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 for detailed information.)

### [Property definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#property_definitions)

We have already learned how to notate properties using the initializer syntax. Oftentimes, there are variables in your code that you would like to put into an object. You will see code like this:

There is a shorter notation available to achieve the same:

#### Duplicate property names

When using the same name for your properties, the second property will overwrite the first.

After ES2015, duplicate property names are allowed everywhere, including [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#duplicate_property_names)
. You can also have duplicate property names in [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
. The only exception is [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
, which must be unique in the class body.

### [Method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#method_definitions)

A property of an object can also refer to a [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 or a [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 or [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 method.

A shorthand notation is available, so that the keyword `function` is no longer necessary.

There is also a way to concisely define generator methods.

Which is equivalent to this ES5-like notation (but note that ECMAScript 5 has no generators):

For more information and examples about methods, see [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
.

### [Computed property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)

The object initializer syntax also supports computed property names. That allows you to put an expression in square brackets `[]`, that will be computed and used as the property name. This is reminiscent of the bracket notation of the [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 syntax, which you may have used to read and set properties already.

Now you can use a similar syntax in object literals, too:

### [Spread properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#spread_properties)

Object literals support the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
. It copies own enumerable properties from a provided object onto a new object.

Shallow-cloning (excluding `prototype`) or merging objects is now possible using a shorter syntax than [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
.

**Warning:** Note that [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
 triggers [setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
, whereas the spread syntax doesn't!

### [Prototype setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#prototype_setter)

A property definition of the form `__proto__: value` or `"__proto__": value` does not create a property with the name `__proto__`. Instead, if the provided value is an object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
, it points the `[[Prototype]]` of the created object to that value. (If the value is not an object or `null`, the object is not changed.)

Note that the `__proto__` key is standardized syntax, in contrast to the non-standard and non-performant [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)
 accessors. It sets the `[[Prototype]]` during object creation, similar to [`Object.create`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
 — instead of mutating the prototype chain.

Only a single prototype setter is permitted in an object literal. Multiple prototype setters are a syntax error.

Property definitions that do not use "colon" notation are not prototype setters. They are property definitions that behave identically to similar definitions using any other name.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object-initializer](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-object-initializer) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
    
*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    
*   [Method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
    
*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/object_initializer/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/object_initializer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FObject_initializer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fobject_initializer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FObject_initializer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fobject_initializer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")