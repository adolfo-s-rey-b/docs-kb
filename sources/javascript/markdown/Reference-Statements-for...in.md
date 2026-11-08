*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#mdn-search)
    

for...in
========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`for...in`** statement iterates over all [enumerable string properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
 of an object (ignoring properties keyed by [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
), including inherited enumerable properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#syntax)

-------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#parameters)

[`variable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#variable)

Receives a string property name on each iteration. May be either a declaration with [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, or [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, or an [assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
 target (e.g., a previously declared variable, an object property, or a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
). Variables declared with `var` are not local to the loop, i.e., they are in the same scope the `for...in` loop is in.

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#object)

Object whose non-symbol enumerable properties are iterated over.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#statement)

A statement to be executed on every iteration. May reference `variable`. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#description)

-----------------------------------------------------------------------------------------------------------------

The loop will iterate over all enumerable properties of the object itself and those the object inherits from its prototype chain (properties of nearer prototypes take precedence over those of prototypes further away from the object in its prototype chain).

Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and goes to the next iteration of the loop.

A `for...in` loop only iterates over enumerable, non-symbol properties. Objects created from built–in constructors like `Array` and `Object` have inherited non–enumerable properties from `Array.prototype` and `Object.prototype`, such as [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
's [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
 method or [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
's [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method, which will not be visited in the `for...in` loop.

The traversal order, as of modern ECMAScript specification, is well-defined and consistent across implementations. Within each component of the prototype chain, all non-negative integer keys (those that can be array indices) will be traversed first in ascending order by value, then other string keys in ascending chronological order of property creation.

The `variable` part of `for...in` accepts anything that can come before the `=` operator. You can use [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
 to declare the variable as long as it's not reassigned within the loop body (it can change between iterations, because those are two separate variables). Otherwise, you can use [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
. You can use [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 to assign multiple local variables, or use a property accessor like `for (x.y in iterable)` to assign the value to an object property. However, [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 and [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
 are not allowed, because the variable is always a string or symbol while these declarations require a disposable object.

A [legacy syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#statements)
 allows `var` declarations of the loop variable to have an initializer. This throws a [syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_for-in_initializer)
 in strict mode and is ignored in non–strict mode.

### [Deleted, added, or modified properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#deleted_added_or_modified_properties)

`for...in` visits property keys in the following fashion:

1.  It first gets all own string keys of the current object, in a fashion very similar to [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)
    .
2.  For each key, if no string with the same value has ever been visited, the [property descriptor is retrieved](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getOwnPropertyDescriptor)
     and the property is only visited if it is enumerable. However, this property string will be marked as visited even if it's not enumerable.
3.  Then, the current object is replaced with its prototype, and the process is repeated.

This means:

*   Any property added to the currently visited object during iteration will not be visited, because all own properties of the current object have already been saved beforehand.
*   If multiple objects in the prototype chain have a property with the same name, only the first one will be considered, and it is only visited if it's enumerable. If it is non-enumerable, no other properties with the same name further up the prototype chain will be visited, even if they are enumerable.

In general, it is best not to add, modify, or remove properties from the object during iteration, other than the property currently being visited. The spec explicitly allows the implementation to not follow the algorithm above in one of the following cases:

*   The object's prototype chain is modified during iteration.
*   A property is deleted from the object or its prototype chain during iteration.
*   A property is added to the object's prototype chain during iteration.
*   A property's enumerability is changed during iteration.

In these cases, implementations may behave differently from what you may expect, or even from each other.

### [Array iteration and for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#array_iteration_and_for...in)

Array indexes are just enumerable properties with integer names and are otherwise identical to general object properties. The `for...in` loop will traverse all integer keys before traversing other keys, and in strictly increasing order, making the behavior of `for...in` close to normal array iteration. However, the `for...in` loop will return all enumerable properties, including those with non–integer names and those that are inherited. Unlike `for...of`, `for...in` uses property enumeration instead of the array's iterator. In [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, `for...of` will visit the empty slots, but `for...in` will not.

It is better to use a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop with a numeric index, [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
, or the [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop, because they will return the index as a number instead of a string, and also avoid non-index properties.

### [Iterating over own properties only](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#iterating_over_own_properties_only)

If you only want to consider properties attached to the object itself, and not its prototypes, you can use one of the following techniques:

*   [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
    
*   [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)
    

`Object.keys` will return a list of enumerable own string properties, while `Object.getOwnPropertyNames` will also contain non-enumerable ones.

Many JavaScript style guides and linters recommend against the use of `for...in`, because it iterates over the entire prototype chain which is rarely what one wants, and may be a confusion with the more widely-used `for...of` loop. `for...in` is most practically used for debugging purposes, being an easy way to check the properties of an object (by outputting to the console or otherwise). In situations where objects are used as ad hoc key-value pairs, `for...in` allows you check if any of those keys hold a particular value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#examples)

-----------------------------------------------------------------------------------------------------------

### [Using for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#using_for...in)

The `for...in` loop below iterates over all of the object's enumerable, non-symbol properties and logs a string of the property names and their values.

### [Iterating own properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#iterating_own_properties)

The following function illustrates the use of [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
: the inherited properties are not displayed.

### [Concurrent modification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#concurrent_modification)

**Warning:** You should not write code like this yourself. It is only included here to illustrate the behavior of `for...in` in some corner cases.

Properties added to the current object during iteration are never visited:

Shadowed properties are only visited once:

In addition, consider the following cases, where the behavior is unspecified, and implementations tend to diverge from the specified algorithm:

Changing the prototype during iteration:

Deleting a property during iteration:

Enumerable properties added to the prototype during iteration:

Changing the enumerability of a property during iteration:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-for-in-and-for-of-statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-for-in-and-for-of-statements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    
*   [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    
*   [Enumerability and ownership of properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
    
*   [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)
    
*   [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
    
*   [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 29, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/for...in/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/for...in (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...in&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor...in%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...in%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor...in%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb6a36de3428f4b42c7707c8f190a349db13bf531%0A*+Document+last+modified%3A+2025-07-29T03%3A29%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")