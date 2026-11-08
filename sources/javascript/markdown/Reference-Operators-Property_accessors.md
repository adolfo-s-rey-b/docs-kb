*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#mdn-search)
    

Property accessors
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Property accessors** provide access to an object's properties by using the dot notation or the bracket notation.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#try_it)

----------------------------------------------------------------------------------------------------------------

    const person1 = {};
    person1["firstName"] = "Mario";
    person1["lastName"] = "Rossi";
    
    console.log(person1.firstName);
    // Expected output: "Mario"
    
    const person2 = {
      firstName: "John",
      lastName: "Doe",
    };
    
    console.log(person2["lastName"]);
    // Expected output: "Doe"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#syntax)

----------------------------------------------------------------------------------------------------------------

js

    object.propertyName
    object[expression]
    object.#privateProperty
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#description)

--------------------------------------------------------------------------------------------------------------------------

One can think of an object as an _associative array_ (a.k.a. _map_, _dictionary_, _hash_, _lookup table_). The _keys_ in this array are the names of the object's [properties](https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript)
.

There are two ways to access properties: _dot notation_ and _bracket notation_.

### [Dot notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#dot_notation)

In the `object.propertyName` syntax, the `propertyName` must be a valid JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 which can also be a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
. For example, `object.$1` is valid, while `object.1` is not.

js

    const variable = object.propertyName;
    object.propertyName = value;
    

js

    const object = {};
    object.$1 = "foo";
    console.log(object.$1); // 'foo'
    

js

    const object = {};
    object.1 = "bar"; // SyntaxError
    console.log(object.1); // SyntaxError
    

Here, the method named `createElement` is retrieved from `document` and is called.

js

    document.createElement("pre");
    

If you use a method for a numeric literal, and the numeric literal has no exponent and no decimal point, you should leave [white-space(s)](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
 before the dot preceding the method call, so that the dot is not interpreted as a decimal point.

js

    77 .toExponential();
    // or
    77
    .toExponential();
    // or
    (77).toExponential();
    // or
    77..toExponential();
    // or
    77.0.toExponential();
    // because 77. === 77.0, no ambiguity
    

In addition, [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 can only be accessed using dot notation within the class that defines them.

### [Bracket notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)

In the `object[expression]` syntax, the `expression` should evaluate to a string or [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
 that represents the property's name. So, it can be any string literal, for example, including `'1foo'`, `'!bar!'`, or even `' '` (a space).

js

    const variable = object[propertyName];
    object[propertyName] = value;
    

This does the exact same thing as the previous example.

js

    document["createElement"]("pre");
    

A space before bracket notation is allowed.

js

    document ["createElement"]("pre");
    

Passing expressions that evaluate to property name will do the same thing as directly passing the property name.

js

    const key = "name";
    const getKey = () => "name";
    const Obj = { name: "Michel" };
    
    Obj["name"]; // returns "Michel"
    Obj[key]; // evaluates to Obj["name"], and returns "Michel"
    Obj[getKey()]; // evaluates to Obj["name"], and returns "Michel"
    

However, beware of using square brackets to access properties whose names are given by external input. This may make your code susceptible to [object injection attacks](https://github.com/eslint-community/eslint-plugin-security/blob/main/docs/the-dangers-of-square-bracket-notation.md "External link (opens in new tab)")
.

### [Property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#property_names)

Each property name is a string or a [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
. Any other value, including a number, is coerced to a string. This outputs `'value'`, since `1` is coerced into `'1'`.

js

    const object = {};
    object["1"] = "value";
    console.log(object[1]);
    

This also outputs `'value'`, since both `foo` and `bar` are converted to the same string (`"[object Object]"`).

js

    const foo = { uniqueProp: 1 };
    const bar = { uniqueProp: 2 };
    const object = {};
    object[foo] = "value";
    console.log(object[bar]);
    

### [Method binding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#method_binding)

It's typical when speaking of an object's properties to make a distinction between properties and methods. However, the property/method distinction is little more than a convention. A method is a property that can be called (for example, if it has a reference to a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 instance as its value).

A method is not bound to the object that it is a property of. Specifically, `this` is not fixed in a method and does not necessarily refer to the object containing the method. Instead, `this` is "passed" by the function call. See [the reference for `this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#examples)

--------------------------------------------------------------------------------------------------------------------

### [Bracket notation vs. eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation_vs._eval)

JavaScript novices often make the mistake of using [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
 where the bracket notation can be used instead.

For example, the following syntax is often seen in many scripts.

js

    const x = eval(`document.forms.form_name.elements.${strFormControl}.value`);
    

`eval()` is slow and should be avoided whenever possible. Also, `strFormControl` would have to hold an identifier, which is not required for names and `id`s of form controls. It is better to use bracket notation instead:

js

    const x = document.forms.form_name.elements[strFormControl].value;
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-property-accessors](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-property-accessors) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
    
*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    
*   [Optional chaining (`?.`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/property_accessors/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/property_accessors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FProperty_accessors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fproperty_accessors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FProperty_accessors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fproperty_accessors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")