*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#mdn-search)
    

Enumerability and ownership of properties
=========================================

Every property in JavaScript objects can be classified by three factors:

*   Enumerable or non-enumerable;
*   String or [symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
    ;
*   Own property or inherited property from the prototype chain.

_Enumerable properties_ are those properties whose internal enumerable flag is set to true, which is the default for properties created via simple assignment or via a property initializer. Properties defined via [`Object.defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 and such are not enumerable by default. Most iteration means (such as [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loops and [`Object.keys`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
) only visit enumerable keys.

Ownership of properties is determined by whether the property belongs to the object directly and not to its prototype chain.

All properties, enumerable or not, string or symbol, own or inherited, can be accessed with [dot notation or bracket notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
. In this section, we will focus on the means provided by JavaScript to visit a group of object properties one-by-one.

[Querying object properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#querying_object_properties)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

There are four built-in ways to query a property of an object. They all support both string and symbol keys. The following table summarizes when each method returns `true`.

|     | Enumerable, own | Enumerable, inherited | Non-enumerable, own | Non-enumerable, inherited |
| --- | --- | --- | --- | --- |
| [`propertyIsEnumerable()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/propertyIsEnumerable) | `true ✅` | `false ❌` | `false ❌` | `false ❌` |
| [`hasOwnProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty) | `true ✅` | `false ❌` | `true ✅` | `false ❌` |
| [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn) | `true ✅` | `false ❌` | `true ✅` | `false ❌` |
| [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in) | `true ✅` | `true ✅` | `true ✅` | `true ✅` |

[Traversing object properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#traversing_object_properties)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are many methods in JavaScript that traverse a group of properties of an object. Sometimes, these properties are returned as an array; sometimes, they are iterated one-by-one in a loop; sometimes, they are used for constructing or mutating another object. The following table summarizes when a property may be visited.

Methods that only visit string properties or only symbol properties will have an extra note. ✅ means a property of this type will be visited; ❌ means it will not.

|     | Enumerable, own | Enumerable, inherited | Non-enumerable, own | Non-enumerable, inherited |
| --- | --- | --- | --- | --- |
| [`Object.keys`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)<br>  <br>[`Object.values`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)<br>  <br>[`Object.entries`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) | ✅  <br>(strings) | ❌   | ❌   | ❌   |
| [`Object.getOwnPropertyNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames) | ✅  <br>(strings) | ❌   | ✅  <br>(strings) | ❌   |
| [`Object.getOwnPropertySymbols`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols) | ✅  <br>(symbols) | ❌   | ✅  <br>(symbols) | ❌   |
| [`Object.getOwnPropertyDescriptors`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptors) | ✅   | ❌   | ✅   | ❌   |
| [`Reflect.ownKeys`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys) | ✅   | ❌   | ✅   | ❌   |
| [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) | ✅  <br>(strings) | ✅  <br>(strings) | ❌   | ❌   |
| [`Object.assign`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)<br>  <br>(After the first parameter) | ✅   | ❌   | ❌   | ❌   |
| [Object spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) | ✅   | ❌   | ❌   | ❌   |

[Obtaining properties by enumerability/ownership](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#obtaining_properties_by_enumerabilityownership)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that this is not the most efficient algorithm for all cases, but useful for a quick demonstration.

*   Detection can occur by `SimplePropertyRetriever.theGetMethodYouWant(obj).includes(prop)`
*   Iteration can occur by `SimplePropertyRetriever.theGetMethodYouWant(obj).forEach((value, prop) => {});` (or use `filter()`, `map()`, etc.)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
    
*   [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
    
*   [`Object.prototype.hasOwnProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)
    
*   [`Object.prototype.propertyIsEnumerable()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/propertyIsEnumerable)
    
*   [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)
    
*   [`Object.getOwnPropertySymbols()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols)
    
*   [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
    
*   [`Object.getOwnPropertyDescriptors()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptors)
    
*   [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
    
*   [`Reflect.ownKeys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/enumerability_and_ownership_of_properties/index.md?plain=1 "Folder: en-us/web/javascript/guide/enumerability_and_ownership_of_properties (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FEnumerability_and_ownership_of_properties&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fenumerability_and_ownership_of_properties%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FEnumerability_and_ownership_of_properties%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fenumerability_and_ownership_of_properties%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")