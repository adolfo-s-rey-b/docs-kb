*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#mdn-search)
    

Destructuring
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **destructuring** syntax is a JavaScript syntax that makes it possible to unpack values from arrays, or properties from objects, into distinct variables. It can be used in locations that receive data (such as the left-hand side of an assignment or anywhere that creates new identifier bindings).

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#try_it)

-----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#syntax)

-----------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#description)

---------------------------------------------------------------------------------------------------------------------

The object and array literal expressions provide an easy way to create _ad hoc_ packages of data.

The destructuring uses similar syntax but uses it on the left-hand side of the assignment instead. It performs the reverse operation of an array declaration, by declaring each element in the collection as a separate variable.

As for objects, compare the two pairs of lines below, and see how there's a direct correspondence within each pair.

This capability is similar to features present in languages such as Perl and Python.

For features specific to array or object destructuring, refer to the individual [examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#examples)
 below.

### [Binding and assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#binding_and_assignment)

For both object and array destructuring, there are two kinds of destructuring patterns: _[binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 pattern_ and _assignment pattern_, with slightly different syntaxes.

In binding patterns, the pattern starts with a declaration keyword (`var`, `let`, or `const`). Then, each individual property must either be bound to a variable or further destructured.

All variables share the same declaration, so if you want some variables to be re-assignable but others to be read-only, you may have to destructure twice — once with `let`, once with `const`.

In many other syntaxes where the language binds a variable for you, you can use a binding destructuring pattern. These include:

*   The looping variable of [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
     [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    , and [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
     loops;
*   [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
     parameters;
*   The [`catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
     binding variable.

In assignment patterns, the pattern does not start with a keyword. Each destructured property is assigned to a target of assignment — which may either be declared beforehand with `var` or `let`, or is a property of another object — in general, anything that can appear on the left-hand side of an assignment expression.

**Note:** The parentheses `( ... )` around the assignment statement are required when using object literal destructuring without a declaration.

`{ a, b } = { a: 1, b: 2 }` is not valid stand-alone syntax, as the `{ a, b }` on the left-hand side is considered a block and not an object literal according to the rules of [expression statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
. However, `({ a, b } = { a: 1, b: 2 })` is valid, as is `const { a, b } = { a: 1, b: 2 }`.

If your coding style does not include trailing semicolons, the `( ... )` expression needs to be preceded by a semicolon, or it may be used to execute a function on the previous line.

Note that the equivalent _binding pattern_ of the code above is not valid syntax:

You can only use assignment patterns as the left-hand side of the [assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
 operator. You cannot use them with compound assignment operators such as `+=` or `*=`.

### [Default value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#default_value)

Each destructured property can have a _default value_. The default value is used when the property is not present, or has value `undefined`. It is not used if the property has value `null`.

The default value can be any expression. It will only be evaluated when necessary.

### [Rest properties and rest elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#rest_properties_and_rest_elements)

You can end a destructuring pattern with a rest property `...rest`. For array destructuring, it collects remaining elements of the iterable into a new array called `rest` (or any name you give it). For object destructuring, it copies all enumerable own properties of the object that are not already picked off by the destructuring pattern into a new object called `rest`.

More formally, the `...rest` syntax is called "rest elements" in array destructuring and "rest properties" in object destructuring, but we often just collectively call them "rest property".

The rest property must be the last in the pattern, and must not have a trailing comma.

Like any other JavaScript language feature, there is no implicit deep-copying. The rest property creates a new object (or array), but all its member values, if they are object references, remain the same.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#examples)

---------------------------------------------------------------------------------------------------------------

### [Array destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#array_destructuring)

#### Basic variable assignment

#### Destructuring with more elements than the source

In an array destructuring from an array of length _N_ specified on the right-hand side of the assignment, if the number of variables specified on the left-hand side of the assignment is greater than _N_, only the first _N_ variables are assigned values. The values of the remaining variables will be undefined.

#### Swapping variables

Two variables values can be swapped in one destructuring expression.

Without destructuring, swapping two values requires a temporary variable (or, in some low-level languages, the [XOR-swap trick](https://en.wikipedia.org/wiki/XOR_swap_algorithm "External link (opens in new tab)")
).

#### Parsing an array returned from a function

It's always been possible to return an array from a function. Destructuring can make working with an array return value more concise.

In this example, `f()` returns the values `[1, 2]` as its output, which can be parsed in a single line with destructuring.

#### Ignoring some returned values

You can ignore return values that you're not interested in:

You can also ignore all returned values:

Though in this case, it's probably clearer to just call the function and not use destructuring at all. You don't have to use the return value.

#### Using a binding pattern as the rest property

The rest property of array destructuring can be another array or object binding pattern. The inner destructuring destructures from the array created after collecting the rest elements, so you cannot access any properties present on the original iterable in this way.

These binding patterns can even be nested, as long as each rest property is the last in the list.

On the other hand, object destructuring can only have an identifier as the rest property.

#### Unpacking values from a regular expression match

When the regular expression [`exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
 method finds a match, it returns an array containing first the entire matched portion of the string and then the portions of the string that matched each parenthesized group in the regular expression. Destructuring allows you to unpack the parts out of this array easily, ignoring the full match if it is not needed.

#### Using array destructuring on any iterable

Array destructuring calls the [iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
 of the right-hand side. Therefore, any iterable, not necessarily arrays, can be destructured.

Non-iterables cannot be destructured as arrays.

Iterables are only iterated until all bindings are assigned.

The rest binding is eagerly evaluated and creates a new array, instead of using the old iterable.

### [Object destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#object_destructuring)

#### Basic assignment

#### Assigning to new variable names

A property can be unpacked from an object and assigned to a variable with a different name than the object property.

Here, for example, `const { p: foo } = o` takes from the object `o` the property named `p` and assigns it to a local variable named `foo`.

#### Assigning to new variable names and providing default values

A property can be both

*   Unpacked from an object and assigned to a variable with a different name.
*   Assigned a default value in case the unpacked value is `undefined`.

#### Unpacking properties from objects passed as a function parameter

Objects passed into function parameters can also be unpacked into variables, which may then be accessed within the function body. As for object assignment, the destructuring syntax allows for the new variable to have the same name or a different name than the original property, and to assign default values for the case when the original object does not define the property.

Consider this object, which contains information about a user.

Here we show how to unpack a property of the passed object into a variable with the same name. The parameter value `{ id }` indicates that the `id` property of the object passed to the function should be unpacked into a variable with the same name, which can then be used within the function.

You can define the name of the unpacked variable. Here we unpack the property named `displayName`, and rename it to `dname` for use within the function body.

Nested objects can also be unpacked. The example below shows the property `fullname.firstName` being unpacked into a variable called `name`.

#### Setting a function parameter's default value

Default values can be specified using `=`, and will be used as variable values if a specified property does not exist in the passed object.

Below we show a function where the default size is `'big'`, default co-ordinates are `x: 0, y: 0` and default radius is 25.

In the function signature for `drawChart` above, the destructured left-hand side has a default value of an empty object `= {}`.

You could have also written the function without that default. However, if you leave out that default value, the function will look for at least one argument to be supplied when invoked, whereas in its current form, you can call `drawChart()` without supplying any parameters. Otherwise, you need to at least supply an empty object literal.

For more information, see [Default parameters > Destructured parameter with default value assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#destructured_parameter_with_default_value_assignment)
.

#### Nested object and array destructuring

#### For of iteration and destructuring

#### Computed object property names and destructuring

Computed property names, like on [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)
, can be used with destructuring.

#### Invalid JavaScript identifier as a property name

Destructuring can be used with property names that are not valid JavaScript [identifiers](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
 by providing an alternative identifier that is valid.

### [Destructuring primitive values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#destructuring_primitive_values)

Object destructuring is almost equivalent to [property accessing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
. This means if you try to destruct a primitive value, the value will get wrapped into the corresponding wrapper object and the property is accessed on the wrapper object.

Same as accessing properties, destructuring `null` or `undefined` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

This happens even when the pattern is empty.

#### Combined array and object destructuring

Array and object destructuring can be combined. Say you want the third element in the array `props` below, and then you want the `name` property in the object, you can do the following:

#### The prototype chain is looked up when the object is deconstructed

When deconstructing an object, if a property is not accessed in itself, it will continue to look up along the prototype chain.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-destructuring-assignment](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-destructuring-assignment) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-destructuring-binding-patterns](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-destructuring-binding-patterns) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#assignment_operators)
    
*   [ES6 in Depth: Destructuring](https://hacks.mozilla.org/2015/05/es6-in-depth-destructuring/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/destructuring/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/destructuring (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FDestructuring&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdestructuring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FDestructuring%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdestructuring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F09893e6f9a71c5955c038aa43e47d446dd92f855%0A*+Document+last+modified%3A+2026-08-10T23%3A01%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")