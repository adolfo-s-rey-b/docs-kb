*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#mdn-search)
    

Map.groupBy()
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** In some versions of some browsers, this method was implemented as the method `Array.prototype.groupToMap()`. Due to web compatibility issues, it is now implemented as a static method. Check the [browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#browser_compatibility)
 for details.

The **`Map.groupBy()`** static method groups the elements of a given iterable using the values returned by a provided callback function. The final returned [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 uses the unique values from the test function as keys, which can be used to get the array of elements in each group.

The method is primarily useful when grouping elements that are associated with an object, and in particular when that object might change over time. If the object is invariant, you might instead represent it using a string, and group elements with [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#try_it)

--------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#syntax)

--------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#parameters)

[`items`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#items)

An [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 (such as an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
) whose elements will be grouped.

[`callbackFn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#callbackfn)

A function to execute for each element in the iterable. It should return a value ([object](https://developer.mozilla.org/en-US/docs/Glossary/Object)
 or [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
) indicating the group of the current element. The function is called with the following arguments:

[`element`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#element)

The current element being processed.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#index)

The index of the current element being processed.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#return_value)

A [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 object with keys for each group, each assigned to an array containing the elements of the associated group.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#description)

------------------------------------------------------------------------------------------------------------------------

`Map.groupBy()` calls a provided `callbackFn` function once for each element in an iterable. The callback function should return a value indicating the group of the associated element. The values returned by `callbackFn` are used as keys for the [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 returned by `Map.groupBy()`. Each key has an associated array containing all the elements for which the callback returned the same value.

The elements in the returned [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 and the original iterable are the same (not [deep copies](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)
). Changing the internal structure of the elements will be reflected in both the original iterable and the returned [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
.

This method is useful when you need to group information that is related to a particular object that might potentially change over time. This is because even if the object is modified, it will continue to work as a key to the returned `Map`. If you instead create a string representation for the object and use that as a grouping key in [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
, you must maintain the mapping between the original object and its representation as the object changes.

**Note:** To access the groups in the returned `Map`, you must use the same object that was originally used as a key in the `Map` (although you may modify its properties). You can't use another object that just happens to have the same name and properties.

`Map.groupBy` does not read the value of `this`. It can be called on any object and a new [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 instance will be returned.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#examples)

------------------------------------------------------------------------------------------------------------------

### [Using Map.groupBy()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#using_map.groupby)

First we define an array containing objects representing an inventory of different foodstuffs. Each food has a `type` and a `quantity`.

The code below uses `Map.groupBy()` with an arrow function that returns the object keys named `restock` or `sufficient`, depending on whether the element has `quantity < 6`. The returned `result` object is a `Map` so we need to call `get()` with the key to obtain the array.

Note that the function argument `{ quantity }` is a basic example of [object destructuring syntax for function arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#unpacking_properties_from_objects_passed_as_a_function_parameter)
. This unpacks the `quantity` property of an object passed as a parameter, and assigns it to a variable named `quantity` in the body of the function. This is a very succinct way to access the relevant values of elements within a function.

The key to a `Map` can be modified and still used. However you can't recreate the key and still use it. For this reason it is important that anything that needs to use the map keeps a reference to its keys.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-map.groupby](https://tc39.es/ecma262/multipage/keyed-collections.html#sec-map.groupby) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Map.groupBy` in `core-js`](https://core-js.io/docs/features/ecmascript/collections#h-map "External link (opens in new tab)")
    
*   [es-shims polyfill of `Map.groupBy`](https://www.npmjs.com/package/map.groupby "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
    
*   [`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
    
*   [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/map/groupby/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/map/groupby (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMap%2FgroupBy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmap%2Fgroupby%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMap%2FgroupBy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmap%2Fgroupby%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")