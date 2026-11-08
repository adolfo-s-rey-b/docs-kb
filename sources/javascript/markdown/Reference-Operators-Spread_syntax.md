*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#mdn-search)
    

Spread syntax (...)
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **spread (`...`)** syntax allows an iterable, such as an array or string, to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected. In an object literal, the spread syntax enumerates the properties of an object and adds the key-value pairs to the object being created.

Spread syntax looks exactly like rest syntax. In a way, spread syntax is the opposite of rest syntax. Spread syntax "expands" an array into its elements, while rest syntax collects multiple elements and "condenses" them into a single element. See [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
 and [rest property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#rest_properties_and_rest_elements)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#try_it)

-----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#syntax)

-----------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#description)

---------------------------------------------------------------------------------------------------------------------

Spread syntax can be used when all elements from an object or array need to be included in a new array or object, or should be applied one-by-one in a function call's arguments list. There are three distinct places that accept the spread syntax:

*   [Function arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_function_calls)
     list (`myFunction(a, ...iterableObj, b)`)
*   [Array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_array_literals)
     (`[1, ...iterableObj, '4', 'five', 6]`)
*   [Object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals)
     (`{ ...obj, key: 'value' }`)

Although the syntax looks the same, they come with slightly different semantics.

Only [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
 values, like [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 and [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
, can be spread in [array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#array_literals)
 and argument lists. Many objects are not iterable, including all [plain objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 that lack a [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 method:

On the other hand, spreading in [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 [enumerates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#traversing_object_properties)
 the own properties of the value. For typical arrays, all indices are enumerable own properties, so arrays can be spread into objects.

All [primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_values)
 can be spread in objects. Only strings have enumerable own properties, and spreading anything else doesn't create properties on the new object.

When using spread syntax for function calls, be aware of the possibility of exceeding the JavaScript engine's argument length limit. See [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 for more details.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#examples)

---------------------------------------------------------------------------------------------------------------

### [Spread in function calls](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_function_calls)

#### Replace apply()

It is common to use [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 in cases where you want to use the elements of an array as arguments to a function.

With spread syntax the above can be written as:

Any argument in the argument list can use spread syntax, and the spread syntax can be used multiple times.

#### Apply for new operator

When calling a constructor with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, it's not possible to **directly** use an array and `apply()`, because `apply()` _calls_ the target function instead of _constructing_ it, which means, among other things, that [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
 will be `undefined`. However, an array can be easily used with `new` thanks to spread syntax:

### [Spread in array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_array_literals)

#### A more powerful array literal

Without spread syntax, the array literal syntax is no longer sufficient to create a new array using an existing array as one part of it. Instead, imperative code must be used using a combination of methods, including [`push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
, [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
, [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
, etc. With spread syntax, this becomes much more succinct:

Just like spread for argument lists, `...` can be used anywhere in the array literal, and may be used more than once.

#### Copying an array

You can use spread syntax to make a [shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 of an array. Each array element retains its identity without getting copied.

Spread syntax effectively goes one level deep while copying an array. Therefore, it may be unsuitable for copying multidimensional arrays. The same is true with [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
 — no native operation in JavaScript does a deep clone. The web API method [`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone "structuredClone()")
 allows deep copying values of certain [supported types](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types)
. See [shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 for more details.

#### A better way to concatenate arrays

[`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 is often used to concatenate an array to the end of an existing array. Without spread syntax, this is done as:

With spread syntax this becomes:

[`Array.prototype.unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)
 is often used to insert an array of values at the start of an existing array. Without spread syntax, this is done as:

With spread syntax, this becomes:

**Note:** Unlike `unshift()`, this creates a new `arr1`, instead of modifying the original `arr1` array in-place.

#### Conditionally adding values to an array

You can make an element present or absent in an array literal, depending on a condition, using a [conditional operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
.

When the condition is `false`, we spread an empty array, so that nothing gets added to the final array. Note that this is different from the following:

In this case, an extra `undefined` element is added when `isSummer` is `false`, and this element will be visited by methods such as [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
.

### [Spread in object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals)

#### Copying and merging objects

You can use spread syntax to merge multiple objects into one new object.

A single spread creates a shallow copy of the original object (but without non-enumerable properties and without copying the prototype), similar to [copying an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#copying_an_array)
.

#### Overriding properties

When one object is spread into another object, or when multiple objects are spread into one object, and properties with identical names are encountered, the property takes the last value assigned while remaining in the position it was originally set.

#### Conditionally adding properties to an object

You can make an element present or absent in an object literal, depending on a condition, using a [conditional operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
.

The case where the condition is `false` is an empty object, so that nothing gets spread into the final object. Note that this is different from the following:

In this case, the `watermelon` property is always present and will be visited by methods such as [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
.

Because primitives can be spread into objects as well, and from the observation that all [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 values do not have enumerable properties, you can simply use a [logical AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)
 operator:

In this case, if `isSummer` is any falsy value, no property will be created on the `fruits` object.

#### Comparing with Object.assign()

Note that [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
 can be used to mutate an object, whereas spread syntax can't.

In addition, [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
 triggers setters on the target object, whereas spread syntax does not.

You cannot naively re-implement the [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
 function through a single spreading:

In the above example, the spread syntax does not work as one might expect: it spreads an _array_ of arguments into the object literal, due to the rest parameter. Here is an implementation of `merge` using the spread syntax, whose behavior is similar to [`Object.assign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
, except that it doesn't trigger setters, nor mutates any object:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-SpreadElement](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-SpreadElement) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ArgumentList](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ArgumentList) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-PropertyDefinition](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-PropertyDefinition) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
    
*   [Rest property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#rest_properties_and_rest_elements)
    
*   [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/spread_syntax/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/spread_syntax (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FSpread_syntax&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fspread_syntax%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FSpread_syntax%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fspread_syntax%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")