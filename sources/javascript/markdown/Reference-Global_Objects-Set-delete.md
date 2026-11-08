*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#mdn-search)
    

Set.prototype.delete()
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`delete()`** method of [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
 instances removes the specified value from this set, if it is in the set.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#try_it)

-------------------------------------------------------------------------------------------------------------

    const set = new Set();
    set.add({ x: 10, y: 20 }).add({ x: 20, y: 30 });
    
    // Delete any point with `x > 10`.
    set.forEach((point) => {
      if (point.x > 10) {
        set.delete(point);
      }
    });
    
    console.log(set.size);
    // Expected output: 1
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#syntax)

-------------------------------------------------------------------------------------------------------------

js

    setInstance.delete(value)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#parameters)

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#value)

The value to remove from the `Set` object. Objects are compared by [reference](https://developer.mozilla.org/en-US/docs/Glossary/Object_reference)
, not by value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#return_value)

`true` if a value in the `Set` object has been removed successfully. `false` if the value is not found in the `Set`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using delete()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#using_delete)

js

    const mySet = new Set();
    mySet.add("foo");
    
    console.log(mySet.delete("bar")); // false; no "bar" element found to be deleted.
    console.log(mySet.delete("foo")); // true; successfully removed.
    
    console.log(mySet.has("foo")); // false; the "foo" element is no longer present.
    

### [Deleting an object from a set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#deleting_an_object_from_a_set)

Because objects are compared by reference, you have to delete them by checking individual properties if you don't have a reference to the original object.

js

    const setObj = new Set(); // Create a new set.
    
    setObj.add({ x: 10, y: 20 }); // Add object in the set.
    
    setObj.add({ x: 20, y: 30 }); // Add object in the set.
    
    // Delete any point with `x > 10`.
    setObj.forEach((point) => {
      if (point.x > 10) {
        setObj.delete(point);
      }
    });
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-set.prototype.delete](https://tc39.es/ecma262/multipage/keyed-collections.html#sec-set.prototype.delete) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
    
*   [`Set.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add)
    
*   [`Set.prototype.clear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/clear)
    
*   [`Set.prototype.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 22, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/set/delete/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/set/delete (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSet%2Fdelete&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fset%2Fdelete%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSet%2Fdelete%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fset%2Fdelete%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7b63b90d24ad8945977bb9dc2735d75f72829bc1%0A*+Document+last+modified%3A+2025-09-22T19%3A21%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")