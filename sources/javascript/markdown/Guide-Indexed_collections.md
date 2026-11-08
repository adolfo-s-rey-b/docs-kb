*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#mdn-search)
    

Indexed collections
===================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections)
    

This chapter introduces collections of data which are ordered by an index value. This includes arrays and array-like constructs such as [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 objects and [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
 objects.

An _array_ is an ordered list of values that you refer to with a name and an index.

For example, consider an array called `emp`, which contains employees' names indexed by their numerical employee number. So `emp[0]` would be employee number zero, `emp[1]` employee number one, and so on.

JavaScript does not have an explicit array data type. However, you can use the predefined `Array` object and its methods to work with arrays in your applications. The `Array` object has methods for manipulating arrays in various ways, such as joining, reversing, and sorting them. It has a property for determining the array length and other properties for use with regular expressions.

We will be focusing on arrays in this article, but many of the same concepts apply to typed arrays as well, since arrays and typed arrays share many similar methods. For more information on typed arrays, see the [typed array guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
.

[Creating an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#creating_an_array)

-------------------------------------------------------------------------------------------------------------------------

The following statements create equivalent arrays:

`element0, element1, …, elementN` is a list of values for the array's elements. When these values are specified, the array is initialized with them as the array's elements. The array's `length` property is set to the number of arguments.

The bracket syntax is called an "array literal" or "array initializer." It's shorter than other forms of array creation, and so is generally preferred. See [Array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#array_literals)
 for details.

To create an array with non-zero length, but without any items, either of the following can be used:

**Note:** In the above code, `arrayLength` must be a `Number`. Otherwise, an array with a single element (the provided value) will be created. Calling `arr.length` will return `arrayLength`, but the array doesn't contain any elements. A [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loop will not find any property on the array.

In addition to a newly defined variable as shown above, arrays can also be assigned as a property of a new or an existing object:

If you wish to initialize an array with a single element, and the element happens to be a `Number`, you must use the bracket syntax. When a single `Number` value is passed to the `Array()` constructor or function, it is interpreted as an `arrayLength`, not as a single element.

This creates an array with only one element: the number 42.

This creates an array with no elements and `arr.length` set to 42.

This is equivalent to:

Calling `Array(N)` results in a `RangeError`, if `N` is a non-whole number whose fractional portion is non-zero. The following example illustrates this behavior.

If your code needs to create arrays with single elements of an arbitrary data type, it is safer to use array literals. Alternatively, create an empty array first before adding the single element to it.

You can also use the [`Array.of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of)
 static method to create arrays with single element.

[Referring to array elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#referring_to_array_elements)

---------------------------------------------------------------------------------------------------------------------------------------------

Because elements are also properties, you can access them using [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
. Suppose you define the following array:

You can refer to the first element of the array as `myArray[0]`, the second element of the array as `myArray[1]`, etc. The index of the elements begins with zero.

**Note:** You can also use [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 to access other properties of the array, like with an object.

[Populating an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#populating_an_array)

-----------------------------------------------------------------------------------------------------------------------------

You can populate an array by assigning values to its elements. For example:

**Note:** If you supply a non-integer value to the array operator in the code above, a property will be created in the object representing the array, instead of an array element.

You can also populate an array when you create it:

### [Understanding length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#understanding_length)

At the implementation level, JavaScript's arrays actually store their elements as standard object properties, using the array index as the property name.

The `length` property is special. Its value is always a positive integer greater than the index of the last element if one exists. (In the example below, `'Dusty'` is indexed at `30`, so `cats.length` returns `30 + 1`).

Remember, JavaScript Array indexes are 0-based: they start at `0`, not `1`. This means that the `length` property will be one more than the highest index stored in the array:

You can also assign to the `length` property.

Writing a value that is shorter than the number of stored items truncates the array. Writing `0` empties it entirely:

### [Iterating over arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#iterating_over_arrays)

A common operation is to iterate over the values of an array, processing each one in some way, as follows:

If you know that none of the elements in your array evaluate to `false` in a boolean context—if your array consists only of [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
 nodes, for example—you can use a more efficient idiom:

This avoids the overhead of checking the length of the array, and ensures that the `div` variable is reassigned to the current item each time around the loop for added convenience.

The [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 method provides another way of iterating over an array:

The function passed to `forEach` is executed once for every item in the array, with the array item passed as the argument to the function. Unassigned values are not iterated in a `forEach` loop.

Note that the elements of an array that are omitted when the array is defined are not listed when iterating by `forEach`, but _are_ listed when `undefined` has been manually assigned to the element:

Since JavaScript array elements are saved as standard object properties, it is not advisable to iterate through JavaScript arrays using [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loops, because normal elements and all enumerable properties will be listed.

### [Array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#array_methods)

The [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 object has the following methods:

The [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 method joins two or more arrays and returns a new array.

The [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
 method joins all elements of an array into a string.

The [`push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
 method adds one or more elements to the end of an array and returns the resulting `length` of the array.

The [`pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
 method removes the last element from an array and returns that element.

The [`shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)
 method removes the first element from an array and returns that element.

The [`unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)
 method adds one or more elements to the front of an array and returns the new length of the array.

The [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
 method extracts a section of an array and returns a new array.

The [`at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at)
 method returns the element at the specified index in the array, or `undefined` if the index is out of range. It's notably used for negative indices that access elements from the end of the array.

The [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method removes elements from an array and (optionally) replaces them. It returns the items which were removed from the array.

The [`reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
 method transposes the elements of an array, in place: the first array element becomes the last and the last becomes the first. It returns a reference to the array.

The [`flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
 method returns a new array with all sub-array elements concatenated into it recursively up to the specified depth.

The [`sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
 method sorts the elements of an array in place, and returns a reference to the array.

`sort()` can also take a callback function to determine how array elements are compared. The callback function is called with two arguments, which are two values from the array. The function compares these two values and returns a positive number, negative number, or zero, indicating the order of the two values. For instance, the following will sort the array by the last letter of a string:

*   if `a` is less than `b` by the sorting system, return `-1` (or any negative number)
*   if `a` is greater than `b` by the sorting system, return `1` (or any positive number)
*   if `a` and `b` are considered equivalent, return `0`.

The [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
 method searches the array for `searchElement` and returns the index of the first match.

The [`lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)
 method works like `indexOf`, but starts at the end and searches backwards.

The [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 method executes `callback` on every array item and returns `undefined`.

The `forEach` method (and others below) that take a callback are known as _iterative methods_, because they iterate over the entire array in some fashion. Each one takes an optional second argument called `thisArg`. If provided, `thisArg` becomes the value of the `this` keyword inside the body of the callback function. If not provided, as with other cases where a function is invoked outside of an explicit object context, `this` will refer to the global object ([`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
, [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
, etc.) when the function is [not strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, or `undefined` when the function is strict.

**Note:** The `sort()` method introduced above is not an iterative method, because its callback function is only used for comparison and may not be called in any particular order based on element order. `sort()` does not accept the `thisArg` parameter either.

The [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
 method returns a new array of the return value from executing `callback` on every array item.

The [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
 method runs `map()` followed by a `flat()` of depth 1.

The [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
 method returns a new array containing the items for which `callback` returned `true`.

The [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
 method returns the first item for which `callback` returned `true`.

The [`findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)
 method returns the last item for which `callback` returned `true`.

The [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
 method returns the index of the first item for which `callback` returned `true`.

The [`findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)
 method returns the index of the last item for which `callback` returned `true`.

The [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
 method returns `true` if `callback` returns `true` for every item in the array.

The [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
 method returns `true` if `callback` returns `true` for at least one item in the array.

The [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 method applies `callback(accumulator, currentValue, currentIndex, array)` for each value in the array for the purpose of reducing the list of items down to a single value. The `reduce` function returns the final value returned by `callback` function.

If `initialValue` is specified, then `callback` is called with `initialValue` as the first parameter value and the value of the first item in the array as the second parameter value.

If `initialValue` is _not_ specified, then `callback`'s first two parameter values will be the first and second elements of the array. On _every_ subsequent call, the first parameter's value will be whatever `callback` returned on the previous call, and the second parameter's value will be the next value in the array.

If `callback` needs access to the index of the item being processed, or access to the entire array, they are available as optional parameters.

The [`reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
 method works like `reduce()`, but starts with the last element.

`reduce` and `reduceRight` are the least obvious of the iterative array methods. They should be used for algorithms that combine two values recursively in order to reduce a sequence down to a single value.

[Array transformations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#array_transformations)

---------------------------------------------------------------------------------------------------------------------------------

You can transform back and forth between arrays and other data structures.

### [Grouping the elements of an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#grouping_the_elements_of_an_array)

The [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
 method can be used to group the elements of an array, using a test function that returns a string indicating the group of the current element.

Here we have an inventory array that contains "food" objects that have a `name` and a `type`.

To use `Object.groupBy()`, you supply a callback function that is called with the current element, and optionally the current index and array, and returns a string indicating the group of the element.

The code below uses an arrow function to return the `type` of each array element (this uses [object destructuring syntax for function arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#unpacking_properties_from_objects_passed_as_a_function_parameter)
 to unpack the `type` element from the passed object). The result is an object that has properties named after the unique strings returned by the callback. Each property is assigned an array containing the elements in the group.

Note that the returned object references the _same_ elements as the original array (not [deep copies](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)
). Changing the internal structure of these elements will be reflected in both the original array and the returned object.

If you can't use a string as the key, for example, if the information to group is associated with an object that might change, then you can instead use [`Map.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)
. This is very similar to `Object.groupBy()` except that it groups the elements of the array into a [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 that can use an arbitrary value ([object](https://developer.mozilla.org/en-US/docs/Glossary/Object)
 or [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
) as a key.

[Sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)

-----------------------------------------------------------------------------------------------------------------

Arrays can contain "empty slots", which are not the same as slots filled with the value `undefined`. Empty slots can be created in one of the following ways:

In some operations, empty slots behave as if they are filled with `undefined`.

But in others (most notably array iteration methods), empty slots are skipped.

For a complete list of how array methods behave with sparse arrays, see [the `Array` reference page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
.

[Multi-dimensional arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#multi-dimensional_arrays)

---------------------------------------------------------------------------------------------------------------------------------------

Arrays can be nested, meaning that an array can contain another array as an element. Using this characteristic of JavaScript arrays, multi-dimensional arrays can be created.

The following code creates a two-dimensional array.

This example creates an array with the following rows:

Row 0: \[0, 0\] \[0, 1\] \[0, 2\] \[0, 3\]
Row 1: \[1, 0\] \[1, 1\] \[1, 2\] \[1, 3\]
Row 2: \[2, 0\] \[2, 1\] \[2, 2\] \[2, 3\]
Row 3: \[3, 0\] \[3, 1\] \[3, 2\] \[3, 3\]

[Using arrays to store other properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#using_arrays_to_store_other_properties)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Arrays can also be used like objects, to store related information.

For example, when an array is the result of a match between a regular expression and a string, the array returns properties and elements that provide information about the match. An array is the return value of [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
, [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
, and [`String.prototype.split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
. For information on using arrays with regular expressions, see [Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
.

[Working with array-like objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#working_with_array-like_objects)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Some JavaScript objects, such as the [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
 returned by [`document.getElementsByTagName()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByTagName)
 or the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object made available within the body of a function, look and behave like arrays on the surface but do not share all of their methods. The `arguments` object provides a [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
 attribute but does not implement array methods like [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
.

Array methods cannot be called directly on array-like objects.

But you can call them indirectly using [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
.

Array prototype methods can be used on strings as well, since they provide sequential access to their characters in a similar way to arrays:

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/indexed_collections/index.md?plain=1 "Folder: en-us/web/javascript/guide/indexed_collections (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIndexed_collections&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Findexed_collections%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIndexed_collections%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Findexed_collections%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe2c34c75df6238fbeff790100cea1ab7e552e49e%0A*+Document+last+modified%3A+2026-09-04T19%3A00%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")