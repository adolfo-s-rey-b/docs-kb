*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#mdn-search)
    

Array.prototype.push()
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`push()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances adds the specified elements to the end of an array and returns the new length of the array.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#try_it)

-------------------------------------------------------------------------------------------------------------

    const animals = ["pigs", "goats", "sheep"];
    
    const count = animals.push("cows");
    console.log(count);
    // Expected output: 4
    console.log(animals);
    // Expected output: Array ["pigs", "goats", "sheep", "cows"]
    
    animals.push("chickens", "cats", "dogs");
    console.log(animals);
    // Expected output: Array ["pigs", "goats", "sheep", "cows", "chickens", "cats", "dogs"]
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#syntax)

-------------------------------------------------------------------------------------------------------------

js

    push()
    push(element1)
    push(element1, element2)
    push(element1, element2, /* …, */ elementN)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#parameters)

[`element1`, …, `elementN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#element1)

The element(s) to add to the end of the array.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#return_value)

The new [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property of the object upon which the method was called.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#description)

-----------------------------------------------------------------------------------------------------------------------

The `push()` method appends values to an array.

[`Array.prototype.unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)
 has similar behavior to `push()`, but applied to the start of an array.

The `push()` method is a [mutating method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods)
. It changes the length and the content of `this`. In case you want the value of `this` to be the same, but return a new array with elements appended to the end, you can use [`arr.concat([element0, element1, /* ... ,*/ elementN])`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 instead. Notice that the elements are wrapped in an extra array — otherwise, if the element is an array itself, it would be spread instead of pushed as a single element due to the behavior of `concat()`.

The `push()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties. Although strings are also array-like, this method is not suitable to be applied on them, as strings are immutable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#examples)

-----------------------------------------------------------------------------------------------------------------

### [Adding elements to an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#adding_elements_to_an_array)

The following code creates the `sports` array containing two elements, then appends two elements to it. The `total` variable contains the new length of the array.

js

    const sports = ["soccer", "baseball"];
    const total = sports.push("football", "swimming");
    
    console.log(sports); // ['soccer', 'baseball', 'football', 'swimming']
    console.log(total); // 4
    

### [Merging two arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#merging_two_arrays)

This example uses [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
 to push all elements from a second array into the first one.

js

    const vegetables = ["parsnip", "potato"];
    const moreVegs = ["celery", "beetroot"];
    
    // Merge the second array into the first one
    vegetables.push(...moreVegs);
    
    console.log(vegetables); // ['parsnip', 'potato', 'celery', 'beetroot']
    

Merging two arrays can also be done with the [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 method, which will make a new combined array instead of adding to the original. The spread syntax only works if the number of elements in the array is less than the maximum number of function arguments allowed by the engine. For longer arrays, use `concat()` or call `push()` multiple times in a loop.

### [Calling push() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#calling_push_on_non-array_objects)

The `push()` method reads the `length` property of `this`. It then sets each index of `this` starting at `length` with the arguments passed to `push()`. Finally, it sets the `length` to the previous length plus the number of pushed elements.

js

    const arrayLike = {
      length: 3,
      unrelated: "foo",
      2: 4,
    };
    Array.prototype.push.call(arrayLike, 1, 2);
    console.log(arrayLike);
    // { '2': 4, '3': 1, '4': 2, length: 5, unrelated: 'foo' }
    
    const plainObj = {};
    // There's no length property, so the length is 0
    Array.prototype.push.call(plainObj, 1, 2);
    console.log(plainObj);
    // { '0': 1, '1': 2, length: 2 }
    

### [Using an object in an array-like fashion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#using_an_object_in_an_array-like_fashion)

As mentioned above, `push` is intentionally generic, and we can use that to our advantage. `Array.prototype.push` can work on an object just fine, as this example shows.

Note that we don't create an array to store a collection of objects. Instead, we store the collection on the object itself and use `call` on `Array.prototype.push` to trick the method into thinking we are dealing with an array—and it just works, thanks to the way JavaScript allows us to establish the execution context in any way we want.

js

    const obj = {
      length: 0,
    
      addElem(elem) {
        // obj.length is automatically incremented
        // every time an element is added.
        [].push.call(this, elem);
      },
    };
    
    // Let's add some empty objects just to illustrate.
    obj.addElem({});
    obj.addElem({});
    console.log(obj.length); // 2
    

Note that although `obj` is not an array, the method `push` successfully incremented `obj`'s `length` property just like if we were dealing with an actual array.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.push](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.push) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.push` in `core-js` with fixes of this method](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.push`](https://www.npmjs.com/package/array.prototype.push "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
    
*   [`Array.prototype.shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)
    
*   [`Array.prototype.unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)
    
*   [`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
    
*   [`Array.prototype.splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/push/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/push (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fpush&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fpush%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fpush%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fpush%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")